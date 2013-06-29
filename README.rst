dj15
----

Demonstrates using templates, including base templates, forms, class based views, and 1.5 features of Django


Below are the base template block variables to replace any defaults with custom data

* load_bootstrap_css = replace this to change the href value of the external stylesheet in ``<head>``
* load_jquery = replace this block to change the src attribute of the ``<script>`` tag to load jquery
* load_bootstrap_js = replace this to change the src attribute of the ``<script>`` tag to load Bootstrap JS files
* default_css_overrides = The default css overrides for all the templates using base
* project_name = Replace this to change the projects name on the upper left side of the page navs
* heading = Replace this to change the heading text on the body of the site
* add_category_form = replace this with the form html content for Category
* add_gallery_form = replace this with the form html content or Gallery
* action_button_text = replace this with the text on the action button that is located on the right side of the site header on the list view pages
* action_button_href = replace this with the location of where the action button should go
* error_notification = replace this with any error notification html text


TODO
-----

* make the model attribute of the classes dynamic
* make the nav model links dynamic


