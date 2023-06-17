function toggleContent(header) {
  const container = header.parentNode;
  const content = container.querySelector('.content');
  const expandIcon = container.querySelector('.expand-icon');
  const megacontainer = container.closest('.megacontainer');

  // Check if the content is currently visible
  const isContentVisible = content.style.display !== 'none';

  // Close all other containers except the clicked one
  const allContainers = document.querySelectorAll('.container');
  allContainers.forEach((c) => {
    if (c !== container) {
      const cContent = c.querySelector('.content');
      const cExpandIcon = c.querySelector('.expand-icon');
      cContent.style.display = 'none';
      cExpandIcon.innerText = '+';
    }
  });

  // Close all other megacontainers except the parent megacontainer
  const allMegaContainers = document.querySelectorAll('.megacontainer');
  allMegaContainers.forEach((mc) => {
    if (mc !== megacontainer) {
      const mcContent = mc.querySelector('.content');
      const mcExpandIcon = mc.querySelector('.expand-icon');
      mcContent.style.display = 'none';
      mcExpandIcon.innerText = '+';
    }
  });

  // Toggle the visibility of the clicked container
  if (!isContentVisible) {
    content.style.display = 'block';
    expandIcon.innerText = '-';
  } else {
    content.style.display = 'none';
    expandIcon.innerText = '+';
  }
}
