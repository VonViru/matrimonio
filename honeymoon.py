<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Luna de Miel — Caro & Diego</title>
<link rel="icon" type="image/svg+xml" href="favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;1,300;1,400&family=Jost:wght@200;300;400&display=swap" rel="stylesheet">
<style>
  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

  :root {
    --cream: #f8f4ef;
    --warm-white: #fdfaf6;
    --stone: #8c8070;
    --dark: #1e1a16;
    --accent: #b8956a;
    --light-stone: #d4c9bc;
  }

  body {
    background: var(--dark);
    color: var(--cream);
    font-family: 'Jost', sans-serif;
    font-weight: 300;
    min-height: 100vh;
    display: grid;
    place-items: center;
    padding: 2rem;
  }

  .lang-toggle {
    position: fixed;
    top: 1.2rem;
    right: 1.5rem;
    display: flex;
    border: 1px solid rgba(184,149,106,0.4);
    background: rgba(30,26,22,0.9);
  }

  .lang-btn {
    padding: 0.35rem 0.75rem;
    font-family: 'Jost', sans-serif;
    font-size: 0.6rem;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    border: none;
    background: transparent;
    color: var(--light-stone);
    cursor: pointer;
  }
  .lang-btn.active { background: var(--accent); color: var(--dark); }

  .back-link {
    position: fixed;
    top: 1.2rem;
    left: 1.5rem;
    font-size: 0.65rem;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: var(--light-stone);
    text-decoration: none;
  }
  .back-link:hover { color: var(--accent); }

  .wrap {
    text-align: center;
    max-width: 460px;
  }

  .eyebrow {
    font-size: 0.75rem;
    letter-spacing: 0.35em;
    text-transform: uppercase;
    color: var(--accent);
    margin-bottom: 1.5rem;
  }

  h1 {
    font-family: 'Cormorant Garamond', serif;
    font-weight: 300;
    font-size: clamp(2.2rem, 7vw, 3rem);
    margin-bottom: 1.5rem;
  }

  .text {
    font-size: 1rem;
    color: var(--light-stone);
    line-height: 1.8;
    margin-bottom: 2.5rem;
  }

  .btn {
    display: inline-block;
    padding: 1.1rem 3rem;
    font-weight: 300;
    font-size: 0.85rem;
    letter-spacing: 0.3em;
    text-transform: uppercase;
    text-decoration: none;
    border: 1px solid var(--accent);
    color: var(--dark);
    background: var(--accent);
    transition: all 0.3s ease;
  }
  .btn:hover { background: transparent; color: var(--accent); }

  .note {
    margin-top: 2rem;
    font-size: 0.75rem;
    color: var(--stone);
  }
</style>
</head>
<body>

<a href="index.html" class="back-link" data-es="← Volver" data-en="← Back" data-fr="← Retour">← Volver</a>

<div class="lang-toggle">
  <button class="lang-btn active" id="btn-es" onclick="setLang('es')">ES</button>
  <button class="lang-btn" id="btn-en" onclick="setLang('en')">EN</button>
  <button class="lang-btn" id="btn-fr" onclick="setLang('fr')">FR</button>
</div>

<div class="wrap">
  <p class="eyebrow" data-es="Luna de Miel" data-en="Honeymoon Fund" data-fr="Voyage de noces">Luna de Miel</p>
  <h1 data-es="Nos vamos a Japón ✈️" data-en="We're off to Japan ✈️" data-fr="On part au Japon ✈️">Nos vamos a Japón ✈️</h1>
  <p class="text" data-es="El mejor regalo es que estés en nuestro casamiento. Si además querés sumarte a esta aventura, cualquier aporte para el viaje lo vamos a atesorar tanto como el brindis." data-en="The best gift is having you at our wedding. If you'd also like to help us kick off this adventure, any contribution towards the trip means the world to us." data-fr="Le plus beau cadeau, c'est votre présence à notre mariage. Si vous souhaitez aussi participer à cette aventure, toute contribution pour le voyage nous touchera énormément.">
    El mejor regalo es que estés en nuestro casamiento. Si además querés sumarte a esta aventura, cualquier aporte para el viaje lo vamos a atesorar tanto como el brindis.
  </p>
  <a href="https://revolut.me/caromanfroni" target="_blank" class="btn" data-es="Contribuir en Revolut" data-en="Contribute via Revolut" data-fr="Contribuer via Revolut">Contribuir en Revolut</a>
  <p class="note" data-es="¿No tenés Revolut? Escribinos y vemos otra forma." data-en="Don't have Revolut? Message us and we'll find another way." data-fr="Pas de Revolut ? Écrivez-nous, on trouvera une solution.">¿No tenés Revolut? Escribinos y vemos otra forma.</p>
</div>

<script>
  function setLang(lang) {
    document.getElementById('btn-es').classList.toggle('active', lang === 'es');
    document.getElementById('btn-en').classList.toggle('active', lang === 'en');
    document.getElementById('btn-fr').classList.toggle('active', lang === 'fr');
    document.querySelectorAll('[data-es]').forEach(el => {
      const val = el.getAttribute('data-' + lang);
      if (val) el.innerHTML = val;
    });
  }
</script>
</body>
</html>
