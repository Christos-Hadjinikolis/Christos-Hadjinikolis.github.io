/*
	Prologue by HTML5 UP
	html5up.net | @ajlkn
	Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)
*/

(function($) {

	skel.breakpoints({
		wide: '(min-width: 961px) and (max-width: 1880px)',
		normal: '(min-width: 961px) and (max-width: 1620px)',
		narrow: '(min-width: 961px) and (max-width: 1320px)',
		narrower: '(max-width: 960px)',
		mobile: '(max-width: 736px)'
	});

	$(function() {

		var	$window = $(window),
			$body = $('body');

		// Theme toggle.
			(function() {
				var storageKey = 'ml-affairs-theme',
					rootEl = document.documentElement,
					toggleEl = document.querySelector('[data-theme-toggle]'),
					labelEl = document.querySelector('[data-theme-toggle-label]');

				if (!toggleEl)
					return;

				var setTheme = function(theme) {
					var isDark = theme === 'dark';

					rootEl.setAttribute('data-theme', theme);
					rootEl.style.colorScheme = theme;
					toggleEl.setAttribute('aria-pressed', isDark ? 'true' : 'false');
					toggleEl.setAttribute('aria-label', isDark ? 'Switch to light mode' : 'Switch to dark mode');

					if (labelEl)
						labelEl.textContent = isDark ? 'Light mode' : 'Dark mode';
				};

				var getStoredTheme = function() {
					try {
						return window.localStorage.getItem(storageKey);
					} catch (error) {
						return null;
					}
				};

				var saveTheme = function(theme) {
					try {
						window.localStorage.setItem(storageKey, theme);
					} catch (error) {}
				};

				setTheme(rootEl.getAttribute('data-theme') || getStoredTheme() || 'dark');

				toggleEl.addEventListener('click', function() {
					var nextTheme = rootEl.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';

					setTheme(nextTheme);
					saveTheme(nextTheme);
				});
			})();

		// Disable animations/transitions until the page has loaded.
			$body.addClass('is-loading');

			$window.on('load', function() {
				$body.removeClass('is-loading');
			});

		// CSS polyfills (IE<9).
			if (skel.vars.IEVersion < 9)
				$(':last-child').addClass('last-child');

		// Fix: Placeholder polyfill.
			$('form').placeholder();

		// Prioritize "important" elements on mobile.
			skel.on('+mobile -mobile', function() {
				$.prioritize(
					'.important\\28 mobile\\29',
					skel.breakpoint('mobile').active
				);
			});

		// Scrolly links.
			$('.scrolly').scrolly();

		// Nav.
			var $nav_a = $('#nav a.scrolly');

			// Scrolly-fy links.
				if($nav_a.scrolly()){
					$nav_a
						.scrolly()
						.on('click', function(e) {

							var t = $(this),
								href = t.attr('href');

							if (href[0] != '#')
								return;

							e.preventDefault();

							// Clear active and lock scrollzer until scrolling has stopped
								$nav_a
									.removeClass('active')
									.addClass('scrollzer-locked');

							// Set this link to active
								t.addClass('active');

						});
				}

			// Initialize scrollzer.
				var ids = [];

				$nav_a.each(function() {

					var href = $(this).attr('href');

					if (href[0] != '#')
						return;

					ids.push(href.substring(1));

				});

				$.scrollzer(ids, { pad: 200, lastHack: true });

			var setOpenYear = function(archiveEl, targetYearEl) {

				if (!archiveEl)
					return;

				var yearEls = archiveEl.querySelectorAll('.nav-year');

				for (var i = 0; i < yearEls.length; i++) {

					var yearEl = yearEls[i],
						toggleEl = yearEl.querySelector('.nav-year__toggle'),
						panelEl = yearEl.querySelector('.nav-year__posts'),
						isOpen = !!targetYearEl && yearEl === targetYearEl;

					if (isOpen)
						yearEl.classList.add('is-open');
					else
						yearEl.classList.remove('is-open');

					if (toggleEl)
						toggleEl.setAttribute('aria-expanded', isOpen ? 'true' : 'false');

					if (panelEl) {
						if (isOpen)
							panelEl.removeAttribute('hidden');
						else
							panelEl.setAttribute('hidden', 'hidden');
					}

				}

			};

			var archiveEls = document.querySelectorAll('#nav [data-nav-blog-archive]');

			for (var archiveIndex = 0; archiveIndex < archiveEls.length; archiveIndex++) {

				var archiveEl = archiveEls[archiveIndex],
					matchLink = null,
					defaultYearEl = null;

				if (window.location.hash)
					matchLink = archiveEl.querySelector('.nav-post-link[href="' + window.location.hash + '"]');

				if (matchLink) {
					setOpenYear(archiveEl, matchLink.closest('.nav-year'));
					continue;
				}

				defaultYearEl = archiveEl.querySelector('.nav-year');

				if (defaultYearEl)
					setOpenYear(archiveEl, defaultYearEl);

			}

			document.addEventListener('click', function(event) {

				var toggleEl = event.target.closest('.nav-year__toggle');

				if (!toggleEl)
					return;

				var archiveEl = toggleEl.closest('[data-nav-blog-archive]'),
					yearEl = toggleEl.closest('.nav-year'),
					isCurrentlyOpen = yearEl && yearEl.classList.contains('is-open');

				if (!archiveEl || !yearEl)
					return;

				event.preventDefault();
				event.stopPropagation();

				if (isCurrentlyOpen)
					setOpenYear(archiveEl, null);
				else
					setOpenYear(archiveEl, yearEl);

			}, true);

		// Header (narrower + mobile).

			// Toggle.
				$(
					'<div id="headerToggle">' +
						'<a href="#header" class="toggle"></a>' +
					'</div>'
				)
					.appendTo($body);

			// Header.
				$('#header')
					.panel({
						delay: 500,
						hideOnClick: true,
						hideOnSwipe: true,
						resetScroll: true,
						resetForms: true,
						side: 'left',
						target: $body,
						visibleClass: 'header-visible'
					});

			// Fix: Remove transitions on WP<10 (poor/buggy performance).
				if (skel.vars.os == 'wp' && skel.vars.osVersion < 10)
					$('#headerToggle, #header, #main')
						.css('transition', 'none');

	});

})(jQuery);
