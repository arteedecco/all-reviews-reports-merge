import logging, sys, glob, click, openpyxl


logging.basicConfig(level=logging.DEBUG)


def find_all_reports(dir):
    reports = {
        'all_reviews': {
            'pattern': '{0}/*_AllReviewsReport_*.xls'.format(dir),
            'files': None
        },
        'all_reviews_by_contributor': {
            'pattern':
                '{0}/*_AllReviewsbyContributorReport_*.xls'.format(dir),
            'files': None
        }
    }
    logging.debug(reports)
    for r in reports:
        logging.debug(r)
        reports[r]['files'] = glob.glob(reports[r]['pattern'])
    logging.debug(reports)


def get_emails():
    pass


def dedupe_emails():
    pass


def merge_emails():
    pass


@click.command()
@click.argument('dir', type=click.Path(exists=True,
                                       writable=True))
def cli(dir="."):
    """"Simple progam that takes Bazaarvoice All Reviews Report, pulls in all
     'User ID' and 'User Email Address' data, de-dupes it and merges it into
      the All Reviews by Contributor report, merging on
      'User ID' and 'Reviewr ID'."""
    logging.debug(dir)
    find_all_reports(dir)


if __name__ == "__main__":
    pass
