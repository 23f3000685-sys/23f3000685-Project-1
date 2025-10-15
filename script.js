window.onload = () => {
  const params = new URLSearchParams(window.location.search);
  const url = params.get('url') || 'sample.png'; // fallback to sample.png
  const img = document.getElementById('captcha');
  img.src = url;

  // Simulate captcha solving (replace with real logic if needed)
  setTimeout(() => {
    document.getElementById('solution').innerText = "Solved: 1234";
  }, 2000); // solve in 2 seconds
};
