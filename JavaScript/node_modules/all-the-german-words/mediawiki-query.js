const request = require('request')
const merge = require('merge')
const Q = require('q')

const DEFAULT_QUERY_PARAMS = {
  action: 'query',
  format: 'json',
  formatversion: 2
}

function WikiQuery (uri) {
  if (!(this instanceof WikiQuery)) return new WikiQuery(uri)
  this.uri = uri
}
WikiQuery.prototype.query = function (params) {
  const fetchPages = continueObject => Q.Promise((resolve, reject, notify) => {
    request({
      method: 'POST',
      uri: this.uri,
      form: merge(true, DEFAULT_QUERY_PARAMS, params, continueObject)
    },
            (err, res, body) => {
              if (err) {
                reject(err)
              }
              if (res.statusCode !== 200) {
                reject(body)
              }
              const json = JSON.parse(body)
              if ((!json.query || !json.query.pages) && !json.batchcomplete) {
                reject(body)
              } else {
                notify((json.query || {}).pages || [])
                resolve(json.continue && fetchPages(json.continue))
              }
            })
  })
  return fetchPages({})
}

module.exports = WikiQuery
