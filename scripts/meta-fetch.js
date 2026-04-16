const https = require('https');

const TOKEN = 'EAAbG6Y0TtiEBRKi9XkBEb0wd55OEHSMXHqA8Acl0TvFheIDvI5wkKNpGAdcjK47BTlZAXxLsgTFZCUS4ZATXBnThyVztfMTFroyOP2EBYb4HZBqH4LMKZB2t6dBpuauPD9YS5snoZCfRVAEequyo7fwft6DzTFhcGMd7TIdq9NmgrvK6yOv796ZC6oSgcyvX3fIw6cZBgrZBPlneAyUHterCTo0BxYZAk3kOnWDWw7krQJZCNXcBdmAV7DNLaHiybmqoUQCJ1xQsVMzy9mTa5CmYTGv';
const ACCOUNT_ID = 'act_255327741430906' + '10';
const SINCE = process.argv[2] || '2026-03-01';
const UNTIL = process.argv[3] || '2026-03-31';

const fields = 'name,status,objective,insights{spend,impressions,reach,clicks,cpc,cpm,cpp,frequency,actions,cost_per_action_type,unique_clicks}';

const params = new URLSearchParams({
  fields: fields,
  time_range: JSON.stringify({ since: SINCE, until: UNTIL }),
  access_token: TOKEN,
  limit: 20
});

const url = 'https://graph.facebook.com/v19.0/' + ACCOUNT_ID + '/campaigns?' + params.toString();

https.get(url, (res) => {
  let data = '';
  res.on('data', c => data += c);
  res.on('end', () => {
    try {
      const json = JSON.parse(data);
      console.log(JSON.stringify(json, null, 2));
    } catch(e) {
      console.log(data);
    }
  });
}).on('error', e => console.error('Error:', e.message));
