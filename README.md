# DrupalSearch
Sublime 3 Plugin helps to search change records of the [Drupal 7 hooks][1] (core and contrib modules).

This package adds:

* A `DrupalSearch` command to the context menu for the selected
* A pallete command for the current selection(or word)
* A pallete command that will ask you what to search within Drupal core
* A pallete command that will ask you what to search within Drupal contrib modules

## Keybindings
For Mac OS X:
- To search from selected text (core hooks):  "ctrl+s"
- To search from user imput (core hooks):  "ctrl+d"
- To search from user imput (contrib modules hooks):  "ctrl+o"

For Linux and Windows:
- To search from selected text (core hooks):  "ctrl+shift+s"
- To search from user imput (core hooks):  "ctrl+shift+d"
- To search from user imput (contrib modules hooks):  "ctrl+shift+o"


## Install
If you're using the [Sublime Package Manger][2] hold down Ctrl+Shift+P and type
`Package Control: Install Package`. Then search for `DrupalSearch` and hit return.

If you're not using the package manager then go to your Sublime packages directory(Sublime Text/Packages) Then run this command `git@github.com:thamanameexusa/DrupalSearch.git`.

Or you can download the package as a zip file [https://github.com/thamanameexusa/DrupalSearch/archive/master.zip][3] then copy it into your Sublime packages directory.


## Settings
```js
{
  "default_browser": "", // chrome, firefox, more valid values here https://docs.python.org/2/library/webbrowser.html#webbrowser.register
  "page_url": "https://www.drupal.org/list-changes" // drupal.org url to perform the search
}
```
You can edit the settings by going to Preferences -> Package Settings -> DrupalSearch -> Settings

## Contributors
- Purushoṭhaman

## License
Copyright (c) 2018 Thaman @DrupalGeeks

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

[1]: https://api.drupal.org/api/drupal/includes!module.inc/group/hooks/7.x
[2]: https://packagecontrol.io
[3]: https://github.com/thamanameexusa/DrupalSearch/archive/master.zip
