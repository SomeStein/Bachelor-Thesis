import numpy as np
from agent import *


class Board:
    def __init__(
        self,
        dimensions,
        sizeExclusion=False,
        neighborhood="von Neumann",
        parallel=False,
    ):
        self.dim = dimensions
        self.SE = sizeExclusion
        self.parallel = parallel
        self.neighborhood = neighborhood

    def __str__(self):
        return f"dimensions: {self.dim}\n size exclusion: {self.SE}\n neighborhood: {self.neighborhood}\n parallel: {self.parallel}"

    def initializeBoard(self, n_agents, n_iter, initial_pos=0):

        self.frames = []
        self.agents = []
        self.added_frames = []
        zero_frame = np.zeros(self.dim, dtype=int)

        for i in range(n_iter):
            self.frames.append(zero_frame.copy())
            self.agents.append([])
            for j in range(n_agents):
                agent = Agent(id, initial_pos[j])
                self.agents[i].append(agent)
                self.frames[i][agent.pos] += 1

        self.frames = np.array(self.added_frames, dtype=int)

    def possibleMoves(self, pos):
        moves = []
        moves.append(pos)
        # if self.SE:

        return moves

    def calculate(self, n_steps, n_iter, n_agents):

        self.initializeBoard(n_agents, n_iter)

        for k in range(n_steps):
            self.added_frames.append(sum(self.frames))
            for i in range(n_iter):
                r.shuffle(self.agents[i])
                for j in range(n_agents):
                    self.agents[i][j].move(
                        self.possibleMoves(self.agents[i][j].pos))

        return np.array(self.added_frames, dtype=int)
