import sublime
import sublime_plugin
import webbrowser
import sys

if sys.version_info < (3, 0):
  from urllib import quote as quote_param
else:
  from urllib.parse import quote_plus as quote_param

def do_search(keyword, is_contrib_search = False):
  settings = sublime.load_settings("DrupalSearch.sublime-settings")
  # Prepare query string.
  query_string = quote_param(keyword)

  page_url = settings.get("page_url", "https://www.drupal.org/list-changes");
  browser = settings.get("browser", "")
  if is_contrib_search:
    fullUrl = page_url + "/" + query_string + "/published"
  else:
    # https://www.drupal.org/list-changes/drupal/published?keywords_description=hook_block_info
    fullUrl = settings.get("page_url", "") + "/drupal/published?keywords_description=%s" % query_string

  if browser:
    try:
      webbrowser.get(browser).open(fullUrl)
    except:
      webbrowser.open(fullUrl)
  else:
    webbrowser.open(fullUrl)

class Drupal8CoreChangeRecordsFromSelectionCommand(sublime_plugin.TextCommand):

  """
  Search the selected text or the current word.
  """
  def run(self, edit):
    #self.view.insert(edit, 0, "Drupal8CoreChangeRecordsCommand\n")
    querys = []
    for region in self.view.sel():
      if region.empty():
        word = self.view.word(region)
        if not word.empty():
          querys.append(self.view.substr(word))
      else:
        if not region.empty():
          querys.append(self.view.substr(region))

    if len(querys) != 0:
      selection = " ".join(querys)
      do_search(selection)
    else:
      sublime.status_message("Nothing to search!")
      self.view.show_popup('<span style="font-size: 10pt">Nothing to search!</span>')

class Drupal8CoreChangeRecordsFromInputCommand(sublime_plugin.WindowCommand):

  """
  A command that prompts the user to enter drupal-core hook to see the change records.
  """
  def run(self):
    def show_input_panel():
      self.window.show_input_panel(
        "Enter a hook name",
        "",
        self.on_done,
        self.on_change,
        self.on_cancel
      )
    sublime.set_timeout(show_input_panel, 10)

  def on_done(self, text):
    do_search(text)

  def on_change(self):
    pass

  def on_cancel(self):
    pass

class Drupal8ContribChangeRecordsCommand(sublime_plugin.WindowCommand):

  """
  A command that prompts the user to enter drupal-contrib module name to see the change records.
  """
  def run(self):
    def show_input_panel():
      self.window.show_input_panel(
        "Enter a module folder name",
        "",
        self.on_done,
        self.on_change,
        self.on_cancel
      )
    sublime.set_timeout(show_input_panel, 10)

  def on_done(self, text):
    is_contrib_search = True
    do_search(text, is_contrib_search)

  def on_change(self):
    pass

  def on_cancel(self):
    pass

