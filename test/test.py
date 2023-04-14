import pytest


class TestPopularity:

    @pytest.mark.parametrize('popularity',
                             [(10 ** 7), (1.5 * 10 ** 7), (5 * 10 ** 7),
                              (10 ** 8), (5 * 10 ** 8), (10 ** 9), (1.5 * 10 ** 8)])
    def test_comparison_popularity(self, popularity, data_from_table):
        exp_popularity = popularity
        errors = []

        for row in data_from_table:
            fact_popularity = row.popularity
            if fact_popularity <= exp_popularity:
                error = f'{row.websites} (Frontend:{",".join(row.frontend)}|Backend:{",".join(row.backend)} ' \
                        f'has {fact_popularity} unique visitors per month. (Expected more than {exp_popularity})'
                errors.append(error)

        assert len(errors) == 0, print('\n'.join(errors))
