var profiles = require('./profiles');
//profiles = JSON.stringify(profiles).replace(/name/g, 'fullname');
profiles = JSON.stringify(profiles)
profiles = JSON.parse(profiles);
//profiles.felix.fullname = "Felix Geisendorfer";
//profiles.felix.name = "Felix Geisendiirfer";
console.log(profiles.felix);