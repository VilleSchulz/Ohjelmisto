const start_year = parseInt(prompt('Give start year'));
const end_year = parseInt(prompt('Give end year'));
let yearList = '';

if (start_year < end_year) {
  for (let i = 0; start_year + i <= end_year; i++) {
    const currentYear = start_year + i;
    if ((currentYear % 4 === 0) && (currentYear % 100 !== 0) ||
        (currentYear % 400 === 0)) {
      yearList += `<li>${start_year + i}</li>`;
    }
  }
} else if (end_year < start_year) {
  for (let i = 0; end_year + i <= start_year; i++) {
    const currentYear = end_year + i;
    if ((currentYear % 4 === 0) && (currentYear % 100 !== 0) ||
        (currentYear % 400 === 0)) {
      yearList += `<li>${end_year + i}</li>`;
    }
  }
}

document.querySelector('.target').innerHTML = yearList;