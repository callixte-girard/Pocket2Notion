# Various notes

This app's purpose is specifically to export your articles from the [Pocket](https://app.getpocket.com/) app to the [Notion](https://notion.so) app.  
If you want to import CSV or plain text, you're not in the good place. Go to [Import2Notion](https://github.com/callixte-girard/Import2Notion).  
Those 2 repositories used to be the same app but I splitted them since April 2020.



# How to proceed ?

### 1) Export your Pocket data in order to use it as an input file for Notion

Go to https://getpocket.com/export and click Export HTML File.

You can also do it manually from the Pocket app : 
Go to your Pocket Settings (click on your profile photo in the upper right corner of the screen) then click on Export.

Don't forget to specify in which path the file is in `constants.py`.


### 2) Create a file containing your credentials

Create the file `static/credentials.py` (in the same folder as `constants.py` and `variables.py`).
Put your `notion_token` and your `notion_coll_url`.

### 3) Customise the program to your needs 

Change the value of `tag_to_search` in `main.py` to specify which tags must be extracted must from the input. Leave blank to extract all.
Change the value of `perform` in `main.py` to answer this question : do you want to Perform the insertion ? or only display the entries that will be inserted in Notion ?
