const start_year = parseInt(prompt('Anna aloitusvuosi'));
const end_year = parseInt(prompt('Anna loppetusvuosi'));

let yearList = '';

if (start_year < end_year) {
  for (let i = 0; start_year + i <= end_year; i++) {
    yearList += `<li>${start_year + i}</li>`;
  }
} else if (end_year < start_year) {
  for (let i = 0; end_year + i <= start_year; i++) {
    yearList += `<li>${end_year + i}</li>`;
  }
}

document.querySelector('.target').innerHTML = yearList;