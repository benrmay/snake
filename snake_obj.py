# snake_obj.py
import pygame


class SnakeSegment:
	def __init__(self, surface, pos):
		self.surface = surface
		self.pos = pos

class Snake(object):
	BLOCK_SIZE = 30
	SEGMENT_SIZE = (BLOCK_SIZE,BLOCK_SIZE)
	color = 0,0,0

	def __init__(self, pos=[0,0]):
		headSurface = pygame.Surface(self.SEGMENT_SIZE)
		headSurface.fill(self.color)

		self.head = SnakeSegment(headSurface, pos)
		self.body = [] # starts off as empty list
	
	def addSegment(self, pos):
		"""
		Add a segment to the self._body
		"""
		newSegment = pygame.Surface(self.SEGMENT_SIZE)
		newSegment.fill(self.color)
		newSegment.scroll(pos[0], pos[1])
		self.body.append(SnakeSegment(newSegment, pos))

	def myGetRect(segment):
		rect = segment.surface.get_rect()
		rect.move_ip(segment.pos) # move the rectangle in place
		return rect

	def redrawSegment(self, segment, display):
		rect = self.myGetRect(segment)
		display.blit(segment.surface, rect)

	def update(self, display):
		self.redraw_segment(self.head, display)
		for segment in self.body:
			segement.redraw_segment(segment, display)

	def move(self, key, display):
		"""
		This is the only function that actually moves the snake
		"""

		# Move the position of the head based on the provided keypress.
				
		oldHeadPos = self.head.pos

		headX, headY = oldHeadPos
		if (key == pygame.K_UP):
			 headY = headY - self.BLOCK_SIZE
		elif (key == pygame.K_DOWN):
			 headY = headY + self.BLOCK_SIZE
		elif (key == pygame.K_LEFT):
			 headX = headX - self.BLOCK_SIZE
		elif (key == pygame.K_RIGHT):
			 headX = headX + self.BLOCK_SIZE
		else:
			 return False # this should never happen

		# make sure the head doesn't go into its own body
		if len(self.body) > 0:
			# move the first segment, and see if it collides with head
			seg1 = self.segments[0]
			mySeg = seg1.surface.get_rect().move(seg1.pos)
			if headRect.move(oldHeadPos).colliderect(mySeg):
				return False # quit the game because yah

		# make sure that the head isn't running out of bounds
		gameRect = display.get_rect() # gives us width and height
		headRect = self.head.surface.get_rect()
		if (headRect.width > gameRect.right or headX < 0):
			print("snake out of bounds horizontally!")
			return False
		elif (headRect.height > gameRect.bottom or headY < 0):
			print("snake out of bounds vertically!")
			return False


		# if everything looks right:
		# update head
		self.head.pos = (headX, headY)
		self.redrawSegment(self.head, display)

		#update the body
		# oldSegmentPos = oldHeadPos
		# for segment in self.body:

		print("move successful")
		return True

