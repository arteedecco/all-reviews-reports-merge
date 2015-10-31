import logging, glob, re, click
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from openpyxl import load_workbook
from xlrd import *


# configure sqlalchemy
Column = Column
Integer = Integer
String = String
Base = declarative_base()
create_engine = create_engine
engine = create_engine('sqlite:///:memory:', echo=True)
Session = sessionmaker(bind=engine)


class UserEmail(Base):
    __tablename__ = 'emails'

    id = Column(Integer, primary_key=True)
    user_id = Column(String(128))
    email = Column(String(320))


Base.metadata.create_all(engine)


# configure logging
logging.basicConfig(level=logging.DEBUG)


def find_all_reports(dir):
    # 'AllReviewsReport', 'AllReviewsbyContributorReport'
    return glob.glob('{0}/*{1}*.xls'.format(dir, 'AllReviewsReport'))


def get_emails(reports):
    """Get all reports, collect all 'User ID' and 'User Email Address'
    values"""
    logging.debug(reports)
    for r in reports:
        wb = open_workbook(r)
        if 'All Reviews Report' in wb.sheet_names():
            ws = wb.sheet_by_name('All Reviews Report')
            logging.debug('cols: {0}, rows: {1}'.format(ws.ncols, ws.nrows))
            logging.debug(ws.name)
            logging.debug(ws.row(3))
            logging.debug(ws.row(3)[0].value)

            email_loc = [{'row': row, 'col': col}
                         for col in range(ws.ncols)
                         for row in range(ws.nrows)
                         if ws.cell_value(row, col) == 'User Email Address']

            if len(email_loc) > 1:
                raise ValueError('More than one column in the All Reviews\
                    Report "{0}" was named "{1}"'.format(
                        r,
                        'User Email Address'))

            userid_loc = [{'row': row, 'col': col}
                          for col in range(ws.ncols)
                          for row in range(ws.nrows)
                          if ws.cell_value(row, col) == 'User ID']

            if len(userid_loc) > 1:
                raise ValueError('More than one column in the All Reviews\
                    Report "{0}" was named "{1}"'.format(
                        r,
                        'User ID'))

            emails = [UserEmail(
                user_id=ws.cell_value(row, userid_loc[0]['col']),
                email=ws.cell_value(row, email_loc[0]['col']))
                for row in range(email_loc[0]['row'] + 1, ws.nrows)]

            logging.debug(emails)



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
    reports = find_all_reports(dir)
    get_emails(reports)


if __name__ == "__main__":
    pass
