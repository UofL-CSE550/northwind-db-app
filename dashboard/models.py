from django.db import models


# Create your models here.
class Customer(models.Model):
    company = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    email_address = models.CharField(max_length=50, blank=True, null=True)
    job_title = models.CharField(max_length=50, blank=True, null=True)
    business_phone = models.CharField(max_length=25, blank=True, null=True)
    home_phone = models.CharField(max_length=25, blank=True, null=True)
    mobile_phone = models.CharField(max_length=25, blank=True, null=True)
    fax_number = models.CharField(max_length=25, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state_province = models.CharField(max_length=50, blank=True, null=True)
    zip_postal_code = models.CharField(max_length=15, blank=True, null=True)
    country_region = models.CharField(max_length=50, blank=True, null=True)
    web_page = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    attachments = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'customers'


class EmployeePrivilege(models.Model):
    employee = models.OneToOneField('Employee', on_delete=models.CASCADE, primary_key=True)
    privilege = models.ForeignKey('Privilege', on_delete=models.CASCADE)

    class Meta:
        db_table = 'employee_privileges'
        unique_together = (('employee', 'privilege'),)


class Employee(models.Model):
    company = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    email_address = models.CharField(max_length=50, blank=True, null=True)
    job_title = models.CharField(max_length=50, blank=True, null=True)
    business_phone = models.CharField(max_length=25, blank=True, null=True)
    home_phone = models.CharField(max_length=25, blank=True, null=True)
    mobile_phone = models.CharField(max_length=25, blank=True, null=True)
    fax_number = models.CharField(max_length=25, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state_province = models.CharField(max_length=50, blank=True, null=True)
    zip_postal_code = models.CharField(max_length=15, blank=True, null=True)
    country_region = models.CharField(max_length=50, blank=True, null=True)
    web_page = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    attachments = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'employees'


class InventoryTransactionType(models.Model):
    id = models.IntegerField(primary_key=True)
    type_name = models.CharField(max_length=50)

    class Meta:
        db_table = 'inventory_transaction_types'


class InventoryTransactions(models.Model):
    transaction_type = models.ForeignKey(InventoryTransactionType,
                                         on_delete=models.CASCADE,
                                         db_column='transaction_type')
    transaction_created_date = models.DateTimeField(blank=True, null=True)
    transaction_modified_date = models.DateTimeField(blank=True, null=True)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    purchase_order = models.ForeignKey('PurchaseOrder',
                                       on_delete=models.CASCADE,
                                       blank=True,
                                       null=True)
    customer_order = models.ForeignKey('Order', on_delete=models.CASCADE, blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'inventory_transactions'


class Invoice(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE, blank=True, null=True)
    invoice_date = models.DateTimeField(blank=True, null=True)
    due_date = models.DateTimeField(blank=True, null=True)
    tax = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    shipping = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    amount_due = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)

    class Meta:
        db_table = 'invoices'


class OrderDetail(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.DecimalField(max_digits=18, decimal_places=4)
    unit_price = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    discount = models.FloatField()
    status = models.ForeignKey('OrderDetailStatus', on_delete=models.CASCADE, blank=True, null=True)
    date_allocated = models.DateTimeField(blank=True, null=True)
    purchase_order_id = models.IntegerField(blank=True, null=True)
    inventory_id = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'order_details'


class OrderDetailStatus(models.Model):
    id = models.IntegerField(primary_key=True)
    status_name = models.CharField(max_length=50)

    class Meta:
        db_table = 'order_details_status'


class Order(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True)
    order_date = models.DateTimeField(blank=True, null=True)
    shipped_date = models.DateTimeField(blank=True, null=True)
    shipper = models.ForeignKey('Shipper', on_delete=models.CASCADE, blank=True, null=True)
    ship_name = models.CharField(max_length=50, blank=True, null=True)
    ship_address = models.TextField(blank=True, null=True)
    ship_city = models.CharField(max_length=50, blank=True, null=True)
    ship_state_province = models.CharField(max_length=50, blank=True, null=True)
    ship_zip_postal_code = models.CharField(max_length=50, blank=True, null=True)
    ship_country_region = models.CharField(max_length=50, blank=True, null=True)
    shipping_fee = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    taxes = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    payment_type = models.CharField(max_length=50, blank=True, null=True)
    paid_date = models.DateTimeField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    tax_rate = models.FloatField(blank=True, null=True)
    tax_status = models.ForeignKey('OrderTaxStatus', on_delete=models.CASCADE, blank=True, null=True)
    status = models.ForeignKey('OrderStatus', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'orders'


class OrderStatus(models.Model):
    id = models.IntegerField(primary_key=True)
    status_name = models.CharField(max_length=50)

    class Meta:
        db_table = 'orders_status'


class OrderTaxStatus(models.Model):
    id = models.IntegerField(primary_key=True)
    tax_status_name = models.CharField(max_length=50)

    class Meta:
        db_table = 'orders_tax_status'


class Privilege(models.Model):
    privilege_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'privileges'


class Product(models.Model):
    supplier_ids = models.TextField(blank=True, null=True)
    product_code = models.CharField(max_length=25, blank=True, null=True)
    product_name = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    standard_cost = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    list_price = models.DecimalField(max_digits=19, decimal_places=4)
    reorder_level = models.IntegerField(blank=True, null=True)
    target_level = models.IntegerField(blank=True, null=True)
    quantity_per_unit = models.CharField(max_length=50, blank=True, null=True)
    discontinued = models.IntegerField()
    minimum_reorder_quantity = models.IntegerField(blank=True, null=True)
    category = models.CharField(max_length=50, blank=True, null=True)
    attachments = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'products'


class PurchaseOrderDetail(models.Model):
    purchase_order = models.ForeignKey('PurchaseOrder', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.DecimalField(max_digits=18, decimal_places=4)
    unit_cost = models.DecimalField(max_digits=19, decimal_places=4)
    date_received = models.DateTimeField(blank=True, null=True)
    posted_to_inventory = models.IntegerField()
    inventory = models.ForeignKey(InventoryTransactions, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'purchase_order_details'


class PurchaseOrderStatus(models.Model):
    id = models.IntegerField(primary_key=True)
    status = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'purchase_order_status'


class PurchaseOrder(models.Model):
    supplier = models.ForeignKey('Supplier', on_delete=models.CASCADE, blank=True, null=True)
    created_by = models.ForeignKey(Employee, on_delete=models.CASCADE, db_column='created_by', blank=True, null=True)
    submitted_date = models.DateTimeField(blank=True, null=True)
    creation_date = models.DateTimeField(blank=True, null=True)
    status = models.ForeignKey(PurchaseOrderStatus, on_delete=models.CASCADE, blank=True, null=True)
    expected_date = models.DateTimeField(blank=True, null=True)
    shipping_fee = models.DecimalField(max_digits=19, decimal_places=4)
    taxes = models.DecimalField(max_digits=19, decimal_places=4)
    payment_date = models.DateTimeField(blank=True, null=True)
    payment_amount = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    payment_method = models.CharField(max_length=50, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    approved_by = models.IntegerField(blank=True, null=True)
    approved_date = models.DateTimeField(blank=True, null=True)
    submitted_by = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'purchase_orders'


class SalesReport(models.Model):
    group_by = models.CharField(primary_key=True, max_length=50)
    display = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    filter_row_source = models.TextField(blank=True, null=True)
    default = models.IntegerField()

    class Meta:
        db_table = 'sales_reports'


class Shipper(models.Model):
    company = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    email_address = models.CharField(max_length=50, blank=True, null=True)
    job_title = models.CharField(max_length=50, blank=True, null=True)
    business_phone = models.CharField(max_length=25, blank=True, null=True)
    home_phone = models.CharField(max_length=25, blank=True, null=True)
    mobile_phone = models.CharField(max_length=25, blank=True, null=True)
    fax_number = models.CharField(max_length=25, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state_province = models.CharField(max_length=50, blank=True, null=True)
    zip_postal_code = models.CharField(max_length=15, blank=True, null=True)
    country_region = models.CharField(max_length=50, blank=True, null=True)
    web_page = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    attachments = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'shippers'


class Strings(models.Model):
    string_id = models.AutoField(primary_key=True)
    string_data = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'strings'


class Supplier(models.Model):
    company = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    email_address = models.CharField(max_length=50, blank=True, null=True)
    job_title = models.CharField(max_length=50, blank=True, null=True)
    business_phone = models.CharField(max_length=25, blank=True, null=True)
    home_phone = models.CharField(max_length=25, blank=True, null=True)
    mobile_phone = models.CharField(max_length=25, blank=True, null=True)
    fax_number = models.CharField(max_length=25, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state_province = models.CharField(max_length=50, blank=True, null=True)
    zip_postal_code = models.CharField(max_length=15, blank=True, null=True)
    country_region = models.CharField(max_length=50, blank=True, null=True)
    web_page = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    attachments = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'suppliers'
