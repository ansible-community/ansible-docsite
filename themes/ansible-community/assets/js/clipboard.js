var clipboard = new ClipboardJS('.btn');

clipboard.on('success', function (e) {
  console.info('Action:', e.action);
  console.info('Text:', e.text);
  console.info('Trigger:', e.trigger);

  // Display the "Copied" popup text
  var popup = document.getElementById('clipboard-popup');
  popup.classList.remove('hidden');

  // Hide after 2 seconds
  setTimeout(function() {
    popup.classList.add('hidden');
  }, 2000);

});

clipboard.on('error', function (e) {
  console.info('Action:', e.action);
  console.info('Text:', e.text);
  console.info('Trigger:', e.trigger);
});
