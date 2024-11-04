from rest_framework.response import Response # type: ignore
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from SistemaRV.decorators import jwt_required
from SistemaRV.decorators import CustomJWTAuthentication
from rest_framework.views import APIView
import boto3
from rest_framework import status

class GeneratePresignedUrlView(APIView):
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = []

    
    @swagger_auto_schema(
        operation_description="Generate a presigned URL to upload a file to S3. If a file with the same name exists, it will be deleted before generating the URL.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['file_name', 'file_type'],
            properties={
                'file_name': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description="The name of the file to be uploaded to S3."
                ),
                'file_type': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description="The MIME type of the file (e.g., image/png, application/pdf)."
                ),
            },
        ),
        responses={
            200: openapi.Response(
                description="Presigned URL generated successfully.",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'url': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description="The generated presigned URL for file upload."
                        ),
                        'file_name': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description="The name of the file to be uploaded."
                        ),
                    }
                )
            ),
            400: openapi.Response(
                description="Bad Request. Missing file name or file type.",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'error': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description="Error message describing the issue."
                        )
                    }
                )
            ),
            500: openapi.Response(
                description="Server Error. Could not check file existence or generate presigned URL.",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'error': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description="Error message describing the server error."
                        )
                    }
                )
            ),
        }
    )
    @jwt_required
    def post(self, request):
        file_name = request.data.get('file_name')
        file_type = request.data.get('file_type')

        if not file_name or not file_type:
            return Response({'error': 'File name and file type are required.'}, status=status.HTTP_400_BAD_REQUEST)

        s3_client = boto3.client(
            's3',
            region_name='us-east-1'
        )

        bucket_name = 'qickartbucket'

        # Check if the file exists
        try:
            s3_client.head_object(Bucket=bucket_name, Key=file_name)
            # If it exists, delete the file
            s3_client.delete_object(Bucket=bucket_name, Key=file_name)
        except s3_client.exceptions.ClientError as e:
            if e.response['Error']['Code'] != '404':
                # If the error is something other than "404 Not Found," return an error
                return Response({'error': 'An error occurred while checking for file existence.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # Generate the presigned URL for uploading
        try:
            presigned_url = s3_client.generate_presigned_url(
                'put_object',
                Params={
                    'Bucket': bucket_name,
                    'Key': file_name,
                    'ContentType': file_type
                },
                ExpiresIn=120  # URL expiration in seconds
            )
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({
            'url': presigned_url,
            'file_name': file_name
        }, status=status.HTTP_200_OK)