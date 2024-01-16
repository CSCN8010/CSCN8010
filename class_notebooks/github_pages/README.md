Thie files in this folder demonstrates:
1. A conversion of a Jupyter notebook into a static HTML
2. Serving this HTML using Github Pages

## Convert the Notebook to an HTML file

1. `jupyter nbconvert --to html NOTEBOOK-PATH --output-dir ./docs/STUDENT-ID --TagRemovePreprocessor.enabled=True --TagRemovePreprocessor.remove_input_tags="['noshow']"` - converts the notebook into an HTML file. `NOTEBOOK-PATH` = the path of the notebook that you want to convert, for example: `./class_notebooks/github_pages/index.ipynb` `STUDENT-ID` should be your student ID, for example `123456`

## Serve the HTML through Github Pages
To serve an HTML through Github pages, you would need to go through the steps below. Once done, the HTML will be public on the internet, with the URL that looks like: `https://GITHUB-USER-NAME.github.io/REPOSITORY-NAME/STUDENT-ID/NOTEBOOK-NAME.html`. For instance: https://conestoga-aaiml-2023-spring.github.io/CSCN8010/instructor/example.html

Steps:
1. In the repostiroy that you'd like to serve content from, click the _settings_ button. In our case, this should be your forked repository:
![image](../../images/github_pages/github_settings_button.jpg)

2. Click on _pages_, and then set the branch to _main_, the folder to _docs_ and click _save_:

![image](../../images/github_pages/enable_github_pages.jpg)



_Note: Reference about Github Pages: [official docs](https://docs.github.com/en/pages/quickstart). Jekyll built-in support: [official docs](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/about-github-pages-and-jekyll)._