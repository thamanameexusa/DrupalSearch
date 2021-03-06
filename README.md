
[![Package Control Downloads][pc-image]][pc-plugin-link]

# DrupalSearch
Sublime 3 Plugin helps to search change records for the [Drupal 7 hooks][drupal-hook-link] (core and contrib modules).

This package adds:

* A `DrupalSearch` command to the context menu for the selected
* A pallete command for the current selection(or word)
* A pallete command that will ask you what to search within Drupal core
* A pallete command that will ask you what to search within Drupal contrib modules

## 🔗 Keybindings
- To search from selected text (core hooks):  `alt+shift+d`, `alt+shift+s`
- To search from user imput (core hooks):  `alt+shift+d`, `alt+shift+i`
- To search from user imput (contrib modules hooks):  `alt+shift+o`, `alt+shift+i`

## 🔗 Install
If you're using the [Sublime Package Manger][pc-link] hold down Ctrl+Shift+P and type
`Package Control: Install Package`. Then search for `DrupalSearch` and hit return.

If you're not using the package manager, go to your Sublime packages directory(Sublime Text/Packages).
Then run this command
> `git clone git@github.com:thamanameexusa/DrupalSearch.git`

Or you can download the package as a zip file [https://github.com/thamanameexusa/DrupalSearch/archive/master.zip][download-link]
Then copy it into your Sublime packages directory.

The `Packages` directory can be found in the following locations:

* OS X:

        ~/Library/Application Support/Sublime Text 2/Packages/
        ~/Library/Application Support/Sublime Text 3/Packages/

* Linux:

        ~/.config/sublime-text-2/Packages/
        ~/.config/sublime-text-3/Packages/

* Windows:

        %APPDATA%/Sublime Text 2/Packages/
        %APPDATA%/Sublime Text 3/Packages/

## 🔗 Settings
```js
{
  "default_browser": "", // chrome, firefox, more valid values here https://docs.python.org/2/library/webbrowser.html#webbrowser.register
  "page_url": "https://www.drupal.org/list-changes" // drupal.org url to perform the search
}
```
You can edit the settings by going to Preferences -> Package Settings -> DrupalSearch -> Settings

## 🔗 Preview
Place cursor inside a word or select some text and press `alt+shift+d`, `alt+shift+s`.
![GIF of the Drupal core hook select and search][preview-gif]

## 🔗 Usage
- Command Pallette
![Screenshot of Command pallette][usage-1-image]

- Context Menu
![Screenshot of Context menu][usage-2-image]

- Press `alt+shift+d`, `alt+shift+i` to search change records of the Drupal core hooks.
![Screenshot of Drupal core hook user input][usage-3-image]

- Press `alt+shift+o`, `alt+shift+i` to search change records of the Drupal contributed modules.
![Screenshot of Drupal contrib module user input][usage-4-image]

㊗️ Happy Searching!

## License
The code is under MIT license:

Copyright (c) 2018 ☮️ [Purushoṭhaman][linkedin-profile-link] [@DrupalGeeks][dgeek-link]

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

## Reference
- [https://github.com/nwjlyons/google-search][reference-1]
- [https://github.com/seregatte/DrupalContribSearch][reference-2]

[pc-link]: https://packagecontrol.io
[pc-image]: https://img.shields.io/packagecontrol/dt/ApplySyntax.svg
[pc-plugin-link]: https://packagecontrol.io/packages/DrupalSearch
[drupal-hook-link]: https://api.drupal.org/api/drupal/includes!module.inc/group/hooks/7.x
[download-link]: https://github.com/thamanameexusa/DrupalSearch/archive/master.zip
[reference-1]: https://github.com/nwjlyons/google-search
[reference-2]: https://github.com/seregatte/DrupalContribSearch
[linkedin-profile-link]: https://www.linkedin.com/in/purushothaman-chinnadurai-ba737171
[dgeek-link]: https://www.drupal.org/u/purushothaman-chinnadurai-drupal-geeks
[preview-gif]: https://i.imgur.com/0fMRKWY.gif
[usage-1-image]: https://i.imgur.com/Nsj2f6G.png
[usage-2-image]: https://i.imgur.com/GJWIOcb.png
[usage-3-image]: https://i.imgur.com/6YyrOSU.png
[usage-4-image]: https://i.imgur.com/X1VGnB2.png
