// Открытие и закрытие мобильного меню.
const burger = document.getElementById('burger');
const mobileMenu = document.getElementById('mobileMenu');
const mobileClose = document.getElementById('mobileClose');

if (burger && mobileMenu) {
  burger.addEventListener('click', function () {
    mobileMenu.classList.add('is-open');
    burger.setAttribute('aria-expanded', 'true');
    document.body.style.overflow = 'hidden';
  });
}

if (mobileClose && mobileMenu) {
  mobileClose.addEventListener('click', function () {
    closeMobileMenu();
  });
}

document.querySelectorAll('.mobile-menu__nav a').forEach(function (link) {
  link.addEventListener('click', function () {
    closeMobileMenu();
  });
});

function closeMobileMenu() {
  if (!mobileMenu || !burger) return;
  mobileMenu.classList.remove('is-open');
  burger.setAttribute('aria-expanded', 'false');
  document.body.style.overflow = '';
}

// Подсветка активной ссылки в верхнем меню.
const currentPath = window.location.pathname;

document.querySelectorAll('.nav__link').forEach(function (link) {
  const href = link.getAttribute('href');

  if (href === currentPath || (currentPath === '/' && href === '/')) {
    link.classList.add('nav__link--active');
  }
});

// Отправка форм заявки без перезагрузки страницы.
document.querySelectorAll('.cta-form, .contact-form').forEach(function (form) {
  form.addEventListener('submit', function (event) {
    event.preventDefault();
    sendContactForm(form);
  });
});

function sendContactForm(form) {
  const message = form.querySelector('.cta-form-message');
  const submitButton = form.querySelector('button[type="submit"]');
  const formData = new FormData(form);

  if (message) {
    message.textContent = 'Отправляем заявку...';
    message.className = 'cta-form-message';
  }

  if (submitButton) {
    submitButton.disabled = true;
  }

  fetch(form.action, {
    method: 'POST',
    body: formData,
    headers: {
      'X-Requested-With': 'XMLHttpRequest'
    }
  })
    .then(function (response) {
      return response.json().then(function (data) {
        return {
          ok: response.ok,
          data: data
        };
      });
    })
    .then(function (result) {
      if (!result.ok) {
        throw new Error('Проверьте имя и телефон.');
      }

      form.reset();

      if (message) {
        message.textContent = result.data.message;
        message.classList.add('is-success');
      }
    })
    .catch(function (error) {
      if (message) {
        message.textContent = error.message;
        message.classList.add('is-error');
      }
    })
    .finally(function () {
      if (submitButton) {
        submitButton.disabled = false;
      }
    });
}
