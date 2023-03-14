const request = require('request')

const atebitsWordsUrl = 'https://github.com/atebits/Words/blob/master/Words/de.txt?raw=true'

request(atebitsWordsUrl, (err, res, data) => {
  if (err) {
    throw err
  }
  if (res.statusCode !== 200) {
    throw res.statusText
  }
  process.stdout.write(data)
})
