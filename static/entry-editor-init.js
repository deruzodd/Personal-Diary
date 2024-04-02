var prevent_leave = true;
window.onbeforeunload = function(e) {
  if (prevent_leave) return '';
}

function saveEntry() {
  prevent_leave = false;
  document.getElementById("save-form").submit();
}
function deleteEntry() {
  prevent_leave = false;
  document.getElementById("delete-form").submit();
}

// TinyMCE setup

const _initial_content =
  document.getElementById('template-data').getAttribute('data-initial-content');
const _theme =
  document.getElementById('template-data').getAttribute('data-theme');
const _font_size =
  document.getElementById('template-data').getAttribute('data-font-size');

tinymce.init({
  selector: '#editor',
  auto_focus: 'editor',
  // for displaying content only
  readonly: false,
  init_instance_callback: function(editor) {
    document.getElementById('loading-editor-spinner').style.display = 'none';
      // set entry content from database
    editor.setContent(_initial_content);

    // use this for autosaving - sends a post request on every change
    // editor.on('Paste Change input Undo Redo', function(e) {
    //   const _csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    //   $.ajax({
    //     url: _url,
    //     headers: {'X-CSRFToken': _csrf_token},
    //     data: {'content': editor.getContent(), 'is_autosave_update': true},
    //     type: "POST",
    //     dataType: 'json',
    //     success: function() {
    //       console.log("Auto saved entry content.")
    //     }
    //   });
    // })
  },
  width: '100%',
  // subtracting navbar height from editor height
  min_height: window.innerHeight - 68,
  resize: false,
  menubar: false,
  contextmenu: false,
  branding: false,
  elementpath: false,
  plugins: [
    'autolink lists image preview emoticons',
    'media paste wordcount',
  ],
  paste_block_drop: true,
  paste_retain_style_properties: '',
  // using custom font sizes
  fontsize_formats: 'Small=12pt Medium=16pt Large=20pt',
  toolbar: 'undo redo | bold italic underline strikethrough ' +
    'backcolor | fontsizeselect | ' + // outdent indent emoticons media
    'bullist emoticons media preview',
  mobile: {
    toolbar_mode: 'wrap',
  },
  // read custom font size from database
  content_style: 'body { ' + //font-family:Helvetica,Arial,sans-serif; ' +
    'font-size: ' + (_font_size == 1 ? '12pt' : (_font_size == 2 ? '16pt' : '20pt')) + '; ' +
    'line-height: 1.2; padding-left: 10px; padding-right: 10px; }',
  // might have problems with caching css when swapping themes later...
  content_css : _theme == 2 ? 'writer-dark' : 'writer',
  skin: _theme == 2 ? 'oxide-dark' : 'oxide',
});
