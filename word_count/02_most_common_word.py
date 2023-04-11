from mrjob.job import MRJob
from mrjob.step import MRStep
import re

WORD_RE = re.compile(r'[\w]+')

class MRMostCommonWOrd(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper,
                   reducer=self.reducer),
            MRStep(mapper=self.mapper_get_keys,
                   reducer=self.reducer_find)
        ]
    def mapper(self, _, line):
        words = WORD_RE.findall(line)
        for word in words:
            yield word.lower(), 1

    def reducer(self, word, counts):
        yield word, sum(counts)

    def mapper_get_keys(self, key, value):
        yield None, (value, key)
    def reducer_find(self, key, values):
        yield max(values)


if __name__ == '__main__':
    MRMostCommonWOrd.run()