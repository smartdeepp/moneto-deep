dump-data:
	python manage.py dumpdata \
	--exclude=wagtailsearch.indexentry \
	--exclude=wagtailsearch.sqliteftsindexentry \
	--exclude=wagtailcore.groupcollectionpermission \
	--exclude=auth.permission \
	--exclude=sessions \
	> data.json


load-data:
	python manage.py migrate
	python manage.py loaddata data.json
	python manage.py update_index
