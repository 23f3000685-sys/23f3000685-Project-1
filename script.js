window.onload = () => {
  const params = new URLSearchParams(window.location.search);
  const url = params.get('url') || 'logo.png'; // fallback to sample.png
  const img = document.getElementById('captcha');
  img.src = url;

  // Simulate captcha solving (replace with real logic if needed)
  setTimeout(() => {
    document.getElementById('solution').innerText = "Solved: 23f3000685";
  }, 2000); // solve in 2 seconds
};
