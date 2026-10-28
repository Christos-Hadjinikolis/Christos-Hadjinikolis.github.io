/* Shared, progressively enhanced navigation drawer. */
(function() {
	'use strict';

	var sidebar = document.querySelector('.site-sidebar'),
		toggle = document.querySelector('[data-sidebar-toggle]'),
		panel = document.getElementById('header');

	if (!sidebar || !toggle || !panel)
		return;

	var hoverMedia = window.matchMedia('(min-width: 961px) and (hover: hover) and (pointer: fine)'),
		isOpen = false,
		isLatched = false,
		overToggle = false,
		overPanel = false,
		openTimer,
		closeTimer;

	function clearTimers() {
		window.clearTimeout(openTimer);
		window.clearTimeout(closeTimer);
	}

	function render() {
		var label = isOpen ? (isLatched ? 'Hide menu' : 'Keep menu open') : 'Show menu';

		document.body.classList.toggle('sidebar-open', isOpen);
		panel.inert = !isOpen;
		panel.setAttribute('aria-hidden', isOpen ? 'false' : 'true');
		toggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
		toggle.setAttribute('aria-label', label);
		toggle.setAttribute('title', label);
	}

	function close() {
		clearTimers();

		// Move focus before making the panel inert, without changing scroll position.
		if (panel.contains(document.activeElement))
			toggle.focus({ preventScroll: true });

		isOpen = false;
		isLatched = false;
		render();
	}

	function scheduleClose() {
		window.clearTimeout(openTimer);
		window.clearTimeout(closeTimer);
		closeTimer = window.setTimeout(function() {
			if (!isLatched && !overToggle && !overPanel && !panel.contains(document.activeElement))
				close();
		}, 250);
	}

	function enter(event) {
		if (event.pointerType !== 'mouse' || !hoverMedia.matches)
			return;

		if (event.currentTarget === toggle)
			overToggle = true;
		else
			overPanel = true;

		clearTimers();

		if (!isOpen) {
			openTimer = window.setTimeout(function() {
				if (overToggle && hoverMedia.matches) {
					isOpen = true;
					render();
				}
			}, 180);
		}
	}

	function leave(event) {
		if (event.pointerType !== 'mouse')
			return;

		if (event.currentTarget === toggle)
			overToggle = false;
		else
			overPanel = false;

		scheduleClose();
	}

	[toggle, panel].forEach(function(element) {
		element.addEventListener('pointerenter', enter);
		element.addEventListener('pointerleave', leave);
	});

	toggle.addEventListener('click', function() {
		clearTimers();

		if (isOpen && isLatched) {
			close();
			return;
		}

		// Clicking a hover preview keeps it open after the pointer moves away.
		isOpen = true;
		isLatched = true;
		render();
	});

	panel.addEventListener('click', function(event) {
		if (event.target.closest('a[href]'))
			close();
	});

	sidebar.addEventListener('focusout', function() {
		window.setTimeout(function() {
			if (!sidebar.contains(document.activeElement))
				scheduleClose();
		}, 0);
	});

	document.addEventListener('click', function(event) {
		if (!sidebar.contains(event.target))
			close();
	});

	document.addEventListener('keydown', function(event) {
		if (event.key === 'Escape') {
			if (isOpen)
				event.preventDefault();
			// Also cancel a hover reveal that has not reached its delay yet.
			close();
		}
	});

	function resetHover() {
		clearTimers();
		overToggle = false;
		overPanel = false;

		if (!isLatched)
			close();
	}

	window.addEventListener('resize', resetHover);
	window.addEventListener('blur', resetHover);
	if (hoverMedia.addEventListener)
		hoverMedia.addEventListener('change', resetHover);

	render();
	document.body.classList.add('sidebar-ready');
})();
