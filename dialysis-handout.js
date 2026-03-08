(function () {
  const apps = {
    chow: { name: 'Benjamin Chow, PA-C', initials: 'BC' },
    cueva: { name: 'Yecenia Cueva, FNP', initials: 'YC' },
    ambriz: { name: 'Sonya Ambriz, FNP', initials: 'SA' },
    parra: { name: 'Gloria Parra, FNP', initials: 'GP' }
  };

  const config = window.DIALYSIS_HANDOUT_CONFIG || {};
  const selectedApp = apps[config.appKey] || apps.chow;
  const unitName = config.unitName || 'Your Dialysis Unit';
  const unitPhone = config.unitPhone || '';
  const unitTel = config.unitTel || unitPhone.replace(/[^\d+]/g, '');
  const hasUnitPhone = Boolean(unitPhone && unitTel);
  const root = document.getElementById('app');

  root.innerHTML = `
    <main class="page">
      <section class="hero">
        <p class="brand"><a class="brand-link" href="https://www.premiernephrologyla.com/" target="_blank" rel="noopener noreferrer">Premier Nephrology Medical Group</a></p>
        <h1 class="hero-title" data-lang="en">Your Dialysis Team and Binder Guide</h1>
        <h1 class="hero-title" data-lang="es">Su Equipo de Diálisis y Guía de Quelantes</h1>
        <p class="hero-copy" data-lang="en">Simple information to help you remember your kidney team and your phosphorus medicine.</p>
        <p class="hero-copy" data-lang="es">Información sencilla para ayudarle a recordar su equipo de riñón y su medicina para el fósforo.</p>
        <div class="brand-meta">
          <a class="brand-chip" href="https://www.premiernephrologyla.com/" target="_blank" rel="noopener noreferrer">PremierNephrologyLA.com</a>
          <span class="brand-chip">1400 S Grand Ave #800</span>
          <a class="brand-chip" href="tel:+12137481414">(213) 748-1414</a>
        </div>
        <p class="unit-badge" data-lang="en">Dialysis Unit: <span>${unitName}</span></p>
        <p class="unit-badge" data-lang="es">Unidad de Diálisis: <span>${unitName}</span></p>
        <div class="lang-toggle" role="group" aria-label="Language">
          <button class="lang-btn active" id="btn-en" type="button">English</button>
          <button class="lang-btn" id="btn-es" type="button">Español</button>
        </div>
      </section>

      <div class="stack">
        <section class="card">
          <h2 class="section-title" data-lang="en">This is your dialysis team</h2>
          <h2 class="section-title" data-lang="es">Este es su equipo de diálisis</h2>
          <p class="section-copy" data-lang="en">If you forget names, this page can help you remember who takes care of you.</p>
          <p class="section-copy" data-lang="es">Si se le olvidan los nombres, esta página puede ayudarle a recordar quién le cuida.</p>
          <div class="team-grid">
            <article class="team-member doctor">
              <div class="avatar" aria-hidden="true">JC</div>
              <div>
                <p class="member-role" data-lang="en">Your Kidney Doctor</p>
                <p class="member-role" data-lang="es">Su Médico de Riñón</p>
                <h3 class="member-name">Jonathan Cheng, MD</h3>
              </div>
            </article>
            <article class="team-member app">
              <div class="avatar" aria-hidden="true">${selectedApp.initials}</div>
              <div>
                <p class="member-role" data-lang="en">Your NP / PA</p>
                <p class="member-role" data-lang="es">Su Enfermera / PA</p>
                <h3 class="member-name">${selectedApp.name}</h3>
              </div>
            </article>
          </div>
        </section>

        <section class="card">
          <h2 class="section-title" data-lang="en">Phosphorus binder basics</h2>
          <h2 class="section-title" data-lang="es">Lo básico sobre los quelantes de fósforo</h2>
          <p class="section-copy" data-lang="en">Dialysis removes some phosphorus, but not enough. High phosphorus can hurt your bones, blood vessels, and heart.</p>
          <p class="section-copy" data-lang="es">La diálisis elimina algo de fósforo, pero no suficiente. El fósforo alto puede dañar sus huesos, vasos sanguíneos y corazón.</p>

          <div class="highlight-grid">
            <div class="highlight teal">
              <h3 data-lang="en">Take binder with food</h3>
              <h3 data-lang="es">Tome el quelante con comida</h3>
              <p data-lang="en">Most binders work only when you take them with a meal or snack.</p>
              <p data-lang="es">La mayoría de los quelantes funcionan solo si los toma con una comida o merienda.</p>
            </div>
            <div class="highlight amber">
              <h3 data-lang="en">Tell us if you skip it</h3>
              <h3 data-lang="es">Avísenos si no lo está tomando</h3>
              <p data-lang="en">Common reasons are cost, constipation, diarrhea, nausea, or forgetting.</p>
              <p data-lang="es">Las razones comunes son costo, estreñimiento, diarrea, náusea o simplemente olvido.</p>
            </div>
            <div class="highlight blue">
              <h3 data-lang="en">Do not change it on your own</h3>
              <h3 data-lang="es">No lo cambie por su cuenta</h3>
              <p data-lang="en">Talk to your dialysis team before stopping or changing the dose.</p>
              <p data-lang="es">Hable con su equipo de diálisis antes de suspenderlo o cambiar la dosis.</p>
            </div>
          </div>

          <div class="pill-grid">
            <article class="pill-card">
              <h3>Calcium Carbonate</h3>
              <p data-lang="en">Chewable. Common first binder. Take with food.</p>
              <p data-lang="es">Masticable. Quelante común. Tómelo con comida.</p>
              <span class="pill-tag" data-lang="en">Examples: Tums, PhosLo</span>
              <span class="pill-tag" data-lang="es">Ejemplos: Tums, PhosLo</span>
            </article>
            <article class="pill-card">
              <h3>Sevelamer</h3>
              <p data-lang="en">No calcium. Swallow whole. Take with food.</p>
              <p data-lang="es">Sin calcio. Se traga entero. Tómelo con comida.</p>
              <span class="pill-tag" data-lang="en">Example: Renvela</span>
              <span class="pill-tag" data-lang="es">Ejemplo: Renvela</span>
            </article>
            <article class="pill-card">
              <h3>Lanthanum</h3>
              <p data-lang="en">Chew it well. Do not swallow whole.</p>
              <p data-lang="es">Debe masticarse bien. No se traga entero.</p>
              <span class="pill-tag" data-lang="en">Example: Fosrenol</span>
              <span class="pill-tag" data-lang="es">Ejemplo: Fosrenol</span>
            </article>
            <article class="pill-card">
              <h3>Ferric Citrate</h3>
              <p data-lang="en">Can also help with anemia. Dark stools can happen.</p>
              <p data-lang="es">También puede ayudar con la anemia. Puede causar heces oscuras.</p>
              <span class="pill-tag" data-lang="en">Example: Auryxia</span>
              <span class="pill-tag" data-lang="es">Ejemplo: Auryxia</span>
            </article>
            <article class="pill-card">
              <h3>Sucroferric</h3>
              <p data-lang="en">Iron-based chewable binder. Dark stools can happen.</p>
              <p data-lang="es">Quelante masticable con hierro. Puede causar heces oscuras.</p>
              <span class="pill-tag" data-lang="en">Example: Velphoro</span>
              <span class="pill-tag" data-lang="es">Ejemplo: Velphoro</span>
            </article>
            <article class="pill-card">
              <h3>Tenapanor</h3>
              <p data-lang="en">Different type. Usually taken before meals. May cause loose stools.</p>
              <p data-lang="es">Tipo diferente. Usualmente antes de comer. Puede causar heces blandas.</p>
              <span class="pill-tag" data-lang="en">Example: Xphozah</span>
              <span class="pill-tag" data-lang="es">Ejemplo: Xphozah</span>
            </article>
          </div>

          <div class="callout" data-lang="en">If you are not sure which binder is yours, show this page to your dialysis nurse or dietitian.</div>
          <div class="callout" data-lang="es">Si no sabe cuál quelante es el suyo, muestre esta página a su enfermera o dietista de diálisis.</div>
        </section>

        <section class="card">
          <h2 class="section-title" data-lang="en">Other important dialysis reminders</h2>
          <h2 class="section-title" data-lang="es">Otros recordatorios importantes de diálisis</h2>
          <ul class="plain-list" data-lang="en">
            <li>Do not miss dialysis unless your dialysis unit tells you what to do.</li>
            <li>Watch salt and fluids so you do not gain too much weight between treatments.</li>
            <li>Ask before starting over-the-counter medicines or supplements.</li>
          </ul>
          <ul class="plain-list" data-lang="es">
            <li>No falte a la diálisis a menos que su unidad le diga qué hacer.</li>
            <li>Cuide la sal y los líquidos para no subir demasiado de peso entre tratamientos.</li>
            <li>Pregunte antes de empezar medicinas o suplementos sin receta.</li>
          </ul>
        </section>

        <section class="card">
          <h2 class="section-title" data-lang="en">Call your dialysis unit if</h2>
          <h2 class="section-title" data-lang="es">Llame a su unidad de diálisis si</h2>
          <ul class="plain-list" data-lang="en">
            <li>You missed a treatment or think you may miss one.</li>
            <li>You ran out of binder pills or cannot afford them.</li>
            <li>Your binder causes bad constipation, diarrhea, nausea, or stomach pain.</li>
            <li>You are not sure which medicines you should be taking.</li>
          </ul>
          <ul class="plain-list" data-lang="es">
            <li>Faltó a un tratamiento o cree que va a faltar.</li>
            <li>Se quedó sin quelantes o no puede pagarlos.</li>
            <li>Su quelante le causa estreñimiento fuerte, diarrea, náusea o dolor de estómago.</li>
            <li>No está seguro de cuáles medicinas debe tomar.</li>
          </ul>

          <div class="contact-row">
            ${hasUnitPhone ? `
              <a class="call-btn" href="tel:${unitTel}">
                <span data-lang="en">Call ${unitName}</span>
                <span data-lang="es">Llame a ${unitName}</span>
              </a>
            ` : `
              <a class="call-btn" href="tel:+12137481414">
                <span data-lang="en">Call Premier Nephrology Office</span>
                <span data-lang="es">Llame a la oficina de Premier Nephrology</span>
              </a>
            `}
            <p class="contact-note" data-lang="en">${hasUnitPhone ? `Dialysis unit phone: ${unitPhone}` : 'Unit-specific phone number not added yet. This button calls the Premier Nephrology office.'}</p>
            <p class="contact-note" data-lang="es">${hasUnitPhone ? `Teléfono de la unidad: ${unitPhone}` : 'Todavía no se ha agregado el teléfono de la unidad. Este botón llama a la oficina de Premier Nephrology.'}</p>
          </div>
        </section>

        <section class="card">
          <h2 class="section-title" data-lang="en">Go to the ER right away if</h2>
          <h2 class="section-title" data-lang="es">Vaya a urgencias de inmediato si</h2>
          <div class="highlight-grid">
            <div class="highlight red">
              <h3 data-lang="en">Trouble breathing</h3>
              <h3 data-lang="es">Le falta el aire</h3>
              <p data-lang="en">Shortness of breath, chest pain, or feeling like you cannot catch your breath.</p>
              <p data-lang="es">Falta de aire, dolor de pecho o sensación de que no puede respirar bien.</p>
            </div>
            <div class="highlight red">
              <h3 data-lang="en">Severe weakness or confusion</h3>
              <h3 data-lang="es">Debilidad severa o confusión</h3>
              <p data-lang="en">If you feel very weak, confused, or hard to wake up.</p>
              <p data-lang="es">Si se siente muy débil, confundido o difícil de despertar.</p>
            </div>
            <div class="highlight red">
              <h3 data-lang="en">Rapid swelling or very fast heartbeat</h3>
              <h3 data-lang="es">Hinchazón rápida o latidos muy rápidos</h3>
              <p data-lang="en">Especially if your legs, feet, or breathing are getting worse quickly.</p>
              <p data-lang="es">Especialmente si sus piernas, pies o respiración empeoran rápidamente.</p>
            </div>
          </div>
        </section>
      </div>

      <p class="footer" data-lang="en">Part of Premier Nephrology Medical Group. This page is for education only and does not replace medical advice from your dialysis team. Visit <a href="https://www.premiernephrologyla.com/" target="_blank" rel="noopener noreferrer">PremierNephrologyLA.com</a>.</p>
      <p class="footer" data-lang="es">Parte de Premier Nephrology Medical Group. Esta página es solo para educación y no reemplaza el consejo médico de su equipo de diálisis. Visite <a href="https://www.premiernephrologyla.com/" target="_blank" rel="noopener noreferrer">PremierNephrologyLA.com</a>.</p>
    </main>
  `;

  const buttonEnglish = document.getElementById('btn-en');
  const buttonSpanish = document.getElementById('btn-es');

  function setLanguage(lang) {
    document.body.dataset.lang = lang;
    document.documentElement.lang = lang;
    buttonEnglish.classList.toggle('active', lang === 'en');
    buttonSpanish.classList.toggle('active', lang === 'es');
    buttonEnglish.setAttribute('aria-pressed', String(lang === 'en'));
    buttonSpanish.setAttribute('aria-pressed', String(lang === 'es'));
    try {
      window.localStorage.setItem('dialysis-handout-lang', lang);
    } catch (error) {
      // Ignore storage failures in restricted browsers.
    }
  }

  buttonEnglish.addEventListener('click', function () { setLanguage('en'); });
  buttonSpanish.addEventListener('click', function () { setLanguage('es'); });

  let savedLanguage = 'en';
  try {
    savedLanguage = window.localStorage.getItem('dialysis-handout-lang') || 'en';
  } catch (error) {
    savedLanguage = 'en';
  }
  setLanguage(savedLanguage === 'es' ? 'es' : 'en');
}());
