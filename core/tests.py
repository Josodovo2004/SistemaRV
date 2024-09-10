from django.test import TestCase
from unittest.mock import patch, MagicMock
from core.models import Item, ItemImpuesto
from core.tasks import darvaloresDeItems

class DarValoresDeItemsTest(TestCase):
    @patch('core.models.Item.objects.get')
    @patch('core.models.ItemImpuesto.objects.filter')
    def test_darvaloresDeItems(self, mock_filter_impuestos, mock_get_item):
        # Mock Item
        mock_item = MagicMock()
        mock_item.valorUnitario = 100.0
        mock_get_item.return_value = mock_item

        # Mock ItemImpuesto
        mock_impuesto = MagicMock()
        mock_impuesto.impuesto.codigo = "01"
        mock_impuesto.impuesto.nombre = "IGV"
        mock_impuesto.impuesto.un_ece_5305 = "VAT"
        mock_impuesto.porcentaje = 0.18

        # Set the mock impuestos
        mock_filter_impuestos.return_value = [mock_impuesto]

        # Serialized data to be passed to the task
        serialized_items = [
            {'id': 1, 'cantidad': 2}  # 2 items, each with a unit price of 100.0
        ]

        # Call the task
        result = darvaloresDeItems(serialized_items)

        # Assertions
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['total_amount'], 236.0)  # (100 * 2) + (100 * 2 * 0.18)
        self.assertEqual(result[0]['paid_amount'], 200.0)   # 100 * 2
        self.assertEqual(result[0]['tax_amount'], 36.0)     # (100 * 2 * 0.18)
        self.assertEqual(result[0]['items'][0]['id'], '01')
        self.assertEqual(result[0]['items'][0]['name'], 'IGV')
        self.assertEqual(result[0]['items'][0]['tax_amount'], 36.0)
