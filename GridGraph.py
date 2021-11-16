from main import LinkedList
from graph import UndirectedGraph
from myQueue import myQueue

DIRECTIONS = {
	'N': (-1, 0),
	'S': (1, 0),
	'W': (0, -1),
	'E': (0, 1)
}

MOVES = {
	'DEFAULT': (DIRECTIONS['E'], DIRECTIONS['S']),
	'RIGHT': (DIRECTIONS['S'], ),
	'BOTTOM': (DIRECTIONS['E'], ),
}

class GridGraph(UndirectedGraph):

	def __init__(self, size):
		super().__init__()
		self.size = size
		self.createVertices()
		currentVertex = self.vertices.head
		while currentVertex is not None:
			self.createEdge(currentVertex)
			currentVertex = currentVertex.next


	def whichBoundary(self, vertex):
		vertexLoc = vertex.data
		# if (vertexLoc[0] == 0 and vertexLoc[1] == 0):
		# 	return 'TOPLEFT'
		# if (vertexLoc[0] == self.size-1 and vertexLoc[1] == 0):
		# 	return 'BOTTOMLEFT'
		if (vertexLoc[0] == self.size-1 and vertexLoc[1] == self.size-1):
			return 'BOTTOMRIGHT'
		# if (vertexLoc[0] == 0 and vertexLoc[1] == self.size-1):
		# 	return 'TOPRIGHT'
		# if (vertexLoc[0] == 0): # top boundary
		# 	return 'TOP'
		# if (vertexLoc[1] == 0): # left boundary
		# 	return 'LEFT'
		if (vertexLoc[0] == self.size-1): # bottom boundary
			return 'BOTTOM'
		if (vertexLoc[1] == self.size-1): # right boundary
			return 'RIGHT'
		return 'DEFAULT'

	def createVertices(self):
		for r in range(self.size):
			for c in range(self.size):
				vertex = UndirectedGraph.Vertex((r, c))
				self.add_vertex(vertex)

	def createEdge(self, vertex):
		vertexLoc = vertex.data
		try:
			boundary = self.whichBoundary(vertex)
			if boundary == 'BOTTOMRIGHT':
				return
			for rowOffset, colOffset in MOVES[boundary]:
				v = self.vertices.find_by_data((vertexLoc[0] + rowOffset, vertexLoc[1] + colOffset))
				edge = UndirectedGraph.Edge(1, vertex, v)
				self.add_edge(edge)
		except KeyError:
			return

	def bfs(self, startVertex, main_surface):
		q = myQueue();
		q.enqueue(LinkedList.Node(startVertex))
		startVertex.visited = True

		while not q.is_empty():
			v = q.dequeue().data
			neighbours = gg.neighbours(v)
			for n in neighbours:
				if not n.visited:
					n.visited = True
					q.enqueue(LinkedList.Node(n))
			showGrid(main_surface, self)

import pygame
import time
from pygame.constants import KEYDOWN, MOUSEBUTTONDOWN, MOUSEMOTION
from pygame.locals import (
	KEYDOWN,
	K_ESCAPE,
	QUIT,
	MOUSEBUTTONUP,
	MOUSEBUTTONDOWN,
	MOUSEMOTION
)
import sys

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
GRID_VERTEX_SIZE = 20
SQUARE_SIZE = int(SCREEN_WIDTH / GRID_VERTEX_SIZE)

def showGrid(main_surface, gg):
	currentVertex = gg.vertices.head
	while currentVertex is not None:
		row, col = currentVertex.data
		
		if currentVertex.visited:
			pygame.draw.rect(main_surface, (255, 0, 0),
				pygame.Rect(col*GRID_VERTEX_SIZE, row*GRID_VERTEX_SIZE, GRID_VERTEX_SIZE, GRID_VERTEX_SIZE))
		else:
			pygame.draw.rect(main_surface, (0, 100, 255),
				pygame.Rect(col*GRID_VERTEX_SIZE, row*GRID_VERTEX_SIZE, GRID_VERTEX_SIZE, GRID_VERTEX_SIZE), 1)
		currentVertex = currentVertex.next
		

if __name__ == '__main__':
	gg = GridGraph(SQUARE_SIZE)

	pygame.init()


	main_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	my_font = pygame.font.SysFont('Courier', 16)

	FPS = 144 # frames per second setting
	fpsClock = pygame.time.Clock()
	frame_count = 0
	frame_rate = 0
	t0 = time.perf_counter()

	toggleFrameRateDisplay = True
	running = True

	start =False
	while running:
		# pygame.time.delay(20)
		for event in pygame.event.get():
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					running = False
				elif event.key == pygame.K_g:
					toggleFrameRateDisplay = not toggleFrameRateDisplay
				elif event.key == pygame.K_SPACE:
					start = True
			elif event.type == QUIT:
				running = False
		
		frame_count += 1
		if frame_count % 500 == 0:
			t1 = time.perf_counter()
			frame_rate = 500 / (t1-t0)
			t0 = t1

		main_surface.fill((255, 255, 255))
		if toggleFrameRateDisplay:
			the_text = my_font.render("Frame = {0}, rate = {1:.2f} fps"
				.format(frame_count, frame_rate), True, (0, 0, 0))
			main_surface.blit(the_text, (10 , 30))
		if start:
			startVertex = gg.vertices.head
			for i in range(SQUARE_SIZE*GRID_VERTEX_SIZE+GRID_VERTEX_SIZE):
				startVertex = startVertex.next
			
			q = myQueue();
			q.enqueue(LinkedList.Node(startVertex))
			startVertex.visited = True

			while not q.is_empty():
				v = q.dequeue().data
				neighbours = gg.neighbours(v)
				for n in neighbours:
					if not n.visited:
						n.visited = True
						q.enqueue(LinkedList.Node(n))
						main_surface.fill((255, 255, 255))
				showGrid(main_surface, gg)
				# pygame.time.delay(1)
				pygame.display.update()
				# fpsClock.tick(FPS)

			# start = False
		else:
			# currentVertex = gg.vertices.head
			# while currentVertex is not None:
			# 	row, col = currentVertex.data
			# 	pygame.draw.rect(main_surface, (0, 0, 0),
			# 		pygame.Rect(col*50, row*50, 50, 50), 1)
			# 	currentVertex = currentVertex.next
			showGrid(main_surface, gg)
			pygame.display.update()
			fpsClock.tick(FPS)

		

		
	pygame.quit()
	sys.exit()