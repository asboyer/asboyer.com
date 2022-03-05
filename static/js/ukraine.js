console.log(window.innerWidth)
if(window.innerWidth > 900) {
    var width = '300px'
    var height = '84px'
    }
else {
    var width = '150px'
    var height = '42px'
}
console.log(width)
var SWU__currentScript = document.currentScript || {};
var SWU__DOMReady = function(callback) {
  document.readyState === 'interactive' || document.readyState === 'complete' ? callback() : document.addEventListener('DOMContentLoaded', callback);
};
SWU__DOMReady(function() {
  const el = document.createElement('div');

  // Options
  const url = SWU__currentScript.getAttribute('url');
  const title = SWU__currentScript.getAttribute('title');
  const position = SWU__currentScript.getAttribute('position');

  // Set custom title
  el.title = title || 'We stand with Ukraine';

  // Set custom URL
  if (url) {
    el.style.cursor = 'pointer'
    el.target = '_blank'
    el.addEventListener('click', function() {
      window.open(url, '_blank')
    })
  }

  // Set custom position (left, right)
  if (position === 'right') {
    el.style.right = '-80px'
    el.style.bottom = '20px'
    el.style.transform = 'rotate(135deg)'
    el.style.background = 'linear-gradient(-360deg, #005BBB 50%, #FFD500 50%)'
  } else {
    el.style.left = '-80px'
    el.style.bottom = '20px'
    el.style.transform = 'rotate(45deg)'
    el.style.background = 'linear-gradient(-180deg, #005BBB 50%, #FFD500 50%)'
  }

  el.style.width = width
  el.style.height = height
  el.style.position = 'fixed';
  el.style.zIndex = '999';

  el.setAttribute('id', 'we-stand-with-ukraine')
  document.body.appendChild(el);
});