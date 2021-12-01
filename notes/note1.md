backup fixtures:
    python manage.py dumpdata pruducts[app name] --format json --indent 4 > products/fixtures/products.json[address]

put the data to new database:
    python manage.py loaddata products/fixtures/pruducts.json