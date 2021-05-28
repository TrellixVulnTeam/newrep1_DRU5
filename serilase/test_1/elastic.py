import elasticsearch


class search(object):
    def twitter_trends(self, index, country):
        real_result = []

        try:
            result = self.es.search(
                index=index,
                body={
                    'query': {
                        'must': {
                            "match": {

                            }
                        }
                    },
                    'size': 20,
                    'from': 0,
                    'sort': {
                        'created_on': {
                            'order': 'desc'
                        }

                    }
                }

            )

            for i in result['hits']['hits']:
                real_result.append(i['_source'])

        except  Exception as error:
            print(error)
