### Folder Twitter

Basically you've got a folder full of pictures, and you want a Twitter account to tweet them on a regular basis, and, like, in a clean way. Randomly, never twice the same picture, and it remains quiet if it has tweeted everything.

Well those scripts, they do that. It's useful, probably.

### Requirements

```bash
$ sudo pip3 install python-twitter
```

### How to use

It is designed to be run from `crontab`. Put the scripts wherever you like, then using `crontab`, fire the following command :

```bash
$ python3 path/to/the/scrip/folder_twitter.py <path_to_the_picture_folder> <path_to_the_credentials>
```

The credentials file should encapsulate your Twitter API credentials and should look as follows, using a JSON structure :

```javascript
{
   "key":"<your API Key>",
   "secret":"<your API Secret>",
   "access_token":"<your Access Token>",
   "access_token_secret":"<your Acess Token Secret>"
}
```
