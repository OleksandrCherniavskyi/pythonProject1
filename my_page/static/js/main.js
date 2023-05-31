function toggleContent(header) {
  const container = header.parentNode;
  const content = container.querySelector('.content');
  const expandIcon = container.querySelector('.expand-icon');

  if (content.style.display === 'none') {
    content.style.display = 'block';
    expandIcon.innerText = '-';
  } else {
    content.style.display = 'none';
    expandIcon.innerText = '+';
  }
}
