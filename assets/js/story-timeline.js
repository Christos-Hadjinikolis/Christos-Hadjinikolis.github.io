/* Native anchors work without JS; enhancement follows reading without scrolling the page. */
(function () {
  'use strict';
  const rail = document.querySelector('[data-story-rail]');
  if (!rail) return;
  const links = Array.from(rail.querySelectorAll('[data-story-point]'));
  const entries = links.map(link => ({link, heading: document.getElementById(link.hash.slice(1))})).filter(x => x.heading);
  if (!entries.length) return;
  const frame = rail.querySelector('[data-story-preview]');
  const nav = rail.querySelector('.story-rail__nav');
  const deck = frame.dataset.deck;
  const wide = window.matchMedia('(min-width:1440px)');
  let current = -1, scheduled = false, loaded = false;
  function preview() {
    if (!rail.open || current < 0) return;
    if (!frame.getAttribute('src')) {
      frame.src = deck + '?preview=1&reveal=all&slide=' + encodeURIComponent(entries[current].link.dataset.slide);
    } else if (loaded) {
      frame.contentWindow.postMessage({kind:'ucl-preview', key:entries[current].link.dataset.slide, step:999}, location.origin);
    }
  }
  frame.addEventListener('load', function () {loaded = true; preview();});
  function select(index) {
    if (index === current) return;
    current = index;
    entries.forEach((entry,i) => i === index ? entry.link.setAttribute('aria-current','location') : entry.link.removeAttribute('aria-current'));
    const active = entries[index].link;
    rail.querySelector('[data-story-current]').textContent = active.dataset.title;
    rail.querySelector('[data-story-summary]').textContent = active.dataset.summary;
    rail.querySelector('[data-story-slide]').href = deck + '?slide=' + encodeURIComponent(active.dataset.slide) + '&reveal=all';
    frame.title = 'Related slide: ' + active.dataset.title;
    rail.querySelector('[data-story-position]').textContent = (index + 1) + ' / ' + entries.length;
    [['prev',index-1],['next',index+1]].forEach(([name,target]) => {
      const link = rail.querySelector('[data-story-'+name+']');
      const valid = target >= 0 && target < entries.length;
      link.href = entries[valid ? target : index].link.hash;
      link.setAttribute('aria-disabled',String(!valid));
      link.tabIndex = valid ? 0 : -1;
    });
    revealActive();
    preview();
  }
  function revealActive() {
    if (!rail.open || current < 0) return;
    const box = nav.getBoundingClientRect(), item = entries[current].link.getBoundingClientRect();
    if (item.top < box.top || item.bottom > box.bottom) nav.scrollTop += item.top - box.top - nav.clientHeight/3;
  }
  function readPosition() {
    scheduled = false;
    const line = Math.min(250,window.innerHeight * .3);
    let index = 0;
    entries.forEach((entry,i) => {if (entry.heading.getBoundingClientRect().top <= line) index = i;});
    select(index);
  }
  function schedule() {if (!scheduled) {scheduled = true; window.requestAnimationFrame(readPosition);}}
  function fit() {rail.open = wide.matches; schedule();}
  rail.addEventListener('toggle',function () {revealActive(); preview();});
  wide.addEventListener('change',fit);
  window.addEventListener('scroll',schedule,{passive:true});
  window.addEventListener('resize',schedule,{passive:true});
  window.addEventListener('load',schedule);
  rail.querySelectorAll('a').forEach(link => link.addEventListener('click',event => {
    if (link.getAttribute('aria-disabled') === 'true') event.preventDefault();
  }));
  fit(); readPosition();
})();
