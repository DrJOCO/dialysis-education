(function () {
  'use strict';

  // Update provider names, credentials, roles, and photo paths here.
  var providers = [
    {
      name: 'Bruce Greenfield, MD',
      initials: 'BG',
      photo: 'Headshots/ProfilePhoto_Greenfield.jpeg',
      type: 'doctor'
    },
    {
      name: 'Leon Rovner, MD',
      initials: 'LR',
      photo: 'Headshots/ProfilePhoto_Rovner.jpeg',
      type: 'doctor'
    },
    {
      name: 'Luani Lee, MD',
      initials: 'LL',
      photo: 'Headshots/ProfilePhoto_Lee.jpeg',
      type: 'doctor'
    },
    {
      name: 'Lin Wang, D.O.',
      initials: 'LW',
      photo: 'Headshots/ProfilePhoto_Wang.jpeg',
      type: 'doctor'
    },
    {
      name: 'Jonathan Cheng, MD, MPH',
      initials: 'JC',
      photo: 'Headshots/ProfilePhoto_Cheng.jpeg',
      type: 'doctor'
    },
    {
      name: 'Yecenia Cueva, FNP-BC',
      initials: 'YC',
      photo: 'Headshots/ProfilePhoto_Yecenia.jpeg',
      type: 'np'
    }
  ];

  var personIcon = '<svg class="sec-icon" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="8" r="4"/><path d="M5 20c0-3.9 3.1-7 7-7s7 3.1 7 7"/></svg>';

  function roleMarkup(type, locale) {
    if (locale === 'ko') {
      return type === 'np' ? '<p class="member-role">전문간호사</p>' : '';
    }

    if (type === 'np') {
      return '<p class="member-role" data-lang="en">Nurse Practitioner</p>' +
        '<p class="member-role" data-lang="es">Enfermera Practicante</p>' +
        '<p class="member-role" data-lang="ko" lang="ko">전문간호사</p>';
    }

    return '';
  }

  function headingMarkup(locale, showIcon) {
    var heading;
    if (locale === 'ko') {
      heading = '<h2 class="section-title">Premier Nephrology 신장 진료팀</h2>';
    } else {
      heading = '<h2 class="section-title" data-lang="en">Your Premier Nephrology kidney team</h2>' +
        '<h2 class="section-title" data-lang="es">Su equipo de riñón de Premier Nephrology</h2>' +
        '<h2 class="section-title" data-lang="ko" lang="ko">Premier Nephrology 콩팥 진료팀</h2>';
    }

    return showIcon ? '<div class="section-head">' + personIcon + heading + '</div>' : heading;
  }

  function introMarkup(locale) {
    if (locale === 'ko') {
      return '<p class="section-copy">진료실, 병원, 또는 투석실에서 이 팀의 여러 의료진을 만날 수 있습니다.</p>';
    }

    return '<p class="section-copy" data-lang="en">You may see different members of this team in the office, hospital, or dialysis unit.</p>' +
      '<p class="section-copy" data-lang="es">Puede ver a diferentes miembros de este equipo en la oficina, el hospital o la unidad de diálisis.</p>' +
      '<p class="section-copy" data-lang="ko" lang="ko">진료실, 병원 또는 투석실에서 이 팀의 여러 의료진을 만날 수 있습니다.</p>';
  }

  function providerMarkup(provider, locale) {
    return '<article class="team-member ' + provider.type + '">' +
      '<div class="provider-photo-wrap">' +
        '<img class="provider-photo" src="' + provider.photo + '" alt="' + provider.name + '">' +
        '<div class="provider-fallback" aria-hidden="true">' + provider.initials + '</div>' +
      '</div>' +
      '<div>' +
        roleMarkup(provider.type, locale) +
        '<h3 class="member-name">' + provider.name + '</h3>' +
      '</div>' +
    '</article>';
  }

  function rosterMarkup(locale, showIcon) {
    return '<section class="card provider-roster">' +
      headingMarkup(locale, showIcon) +
      introMarkup(locale) +
      '<div class="team-grid provider-grid">' +
        providers.map(function (provider) { return providerMarkup(provider, locale); }).join('') +
      '</div>' +
    '</section>';
  }

  function showFallback(image) {
    image.style.display = 'none';
    image.nextElementSibling.style.display = 'flex';
  }

  document.querySelectorAll('[data-provider-roster]').forEach(function (placeholder) {
    var locale = placeholder.getAttribute('data-provider-locale') === 'ko' ? 'ko' : 'en-es';
    var showIcon = placeholder.getAttribute('data-provider-icon') !== 'false';
    var container = document.createElement('div');
    container.innerHTML = rosterMarkup(locale, showIcon);
    var roster = container.firstElementChild;
    placeholder.parentNode.replaceChild(roster, placeholder);

    roster.querySelectorAll('.provider-photo').forEach(function (image) {
      image.addEventListener('error', function () { showFallback(image); });
      if (image.complete && image.naturalWidth === 0) showFallback(image);
    });
  });
})();
