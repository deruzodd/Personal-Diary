
// dashboard scripts

function reverseEntrySortOrder() {
  document.getElementById('entry-list-wrapper').classList
    .toggle('flex-column');
  document.getElementById('entry-list-wrapper').classList
    .toggle('flex-column-reverse');
}

// base template scripts

var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
  return new bootstrap.Tooltip(tooltipTriggerEl);
});
