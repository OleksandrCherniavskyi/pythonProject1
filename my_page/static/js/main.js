

function toggleContent(header) {
  const container = header.parentNode;
  const content = container.querySelector('.content');
  const expandIcon = container.querySelector('.expand-icon')
  // Check if the content is currently visible
  const isContentVisible = content.style.display !== 'none'
  // Hide all other content elements except the clicked one
  const allContainers = document.querySelectorAll('.container');
  allContainers.forEach((container) => {
    const content = container.querySelector('.content');
    const expandIcon = container.querySelector('.expand-icon')
    if (container !== header.parentNode) {
      content.style.display = 'none';
      expandIcon.innerText = '+';
    }
  })
  // Toggle the visibility of the clicked container
  if (!isContentVisible) {
    content.style.display = 'block';
    expandIcon.innerText = '-';
  } else {
    content.style.display = 'none';
    expandIcon.innerText = '+';
  }
}

