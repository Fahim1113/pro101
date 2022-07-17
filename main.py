import dropbox

class TransferData:
  def __init__(self, access_token):
    self.access_token = access_token

  def upload_file(self, file_from, file_to):
    dbx = dropbox.Dropbox(self.access_token)


    f = open(file_from, 'rb')
    dbx.files_upload(f.read(), file_to)

def main():
  access_token = 'sl.BLn7CK4ChMpee5dcxfizZL5z7GHvCFcsqqyv_UCk-EsJNIlAA_rGxsmGGAQ3MEv3hNDIv4c48rVSSm6OUGojNADIQ7xvPhDXkqHZeadepFULiwzFh8IIRigg97pcFR5N9gUemlD6'
  transferData = TransferData(access_token)

  file_from = input("File to copy:")
  file_to = input("Where it is going to be in dropbox:")
  # API v2
  transferData.upload_file(file_from, file_to)
  print("file has been moved !!!")


main()