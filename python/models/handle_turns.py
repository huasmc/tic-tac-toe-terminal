class HandleTurns:

  def __init__(self):
      self.currentPlayerToken = None

  def change(self):
      if( self.currentPlayerToken == 'X' ):
          self.set_currentPlayerToken('O')
      else:
          self.set_currentPlayerToken('X')

  def set_currentPlayerToken(self, token):
      self.currentPlayerToken = token
