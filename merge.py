import logging, sys, glob, re, click, openpyxl


logging.basicConfig(level=logging.DEBUG)


def find_all_reports(dir):
    # 'AllReviewsReport', 'AllReviewsbyContributorReport'
    all_reviews_reports = glob.glob(
        '{0}/*{1}*.xls'.format(dir, 'AllReviewsReport'))
    logging.debug(all_reviews_reports)
    # find matching AllReviewsbyContributorReport
    for r in all_reviews_reports:
        fname = re.sub('{0}/'.format(dir), '', r)
        logging.debug(fname)
        mname = re.sub('AllReviewsReport',
                       'AllReviewsbyContributorReport',
                       fname)
        logging.debug(mname)



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
