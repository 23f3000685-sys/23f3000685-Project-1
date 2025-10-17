window.onload = () => {
  const params = new URLSearchParams(window.location.search);
  const url = params.get('url') || 'logo.png';
  const img = document.getElementById('captcha');
  img.src = url;

  // Simulate captcha solving
  setTimeout(() => {
    document.getElementById('solution').innerText = "Solved: 23f3000685";
  }, 2000);
};
