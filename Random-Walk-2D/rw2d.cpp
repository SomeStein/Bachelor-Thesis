#include <iostream>
#include <cstdlib>

// PULL PARAMETERS FROM EXTERNAL FILE
const int n_walkers = 10;
const int n_steps = 1000;
const int n_iterations = 1000;
const int rowCount = 10;
const int colCount = 10;
int initial_data[n_walkers][2];

// class of Agent
class Walker
{
public:
   int posx = 0;
   int posy = 0;

   void move(bool size_exclusion, int board[rowCount][colCount])
   {

      // get random step direction
      int stepx = 0, stepy = 0;
      stepx += rand() % 4 - 1;
      if (stepx == 0)
      {
         stepy += rand() % 3 - 1;
      };
      if (stepx == 2)
      {
         stepx = 0;
         stepy += rand() % 3 - 1;
      };

      // check if chosen step is free only when size exclusion is enabled
      if (size_exclusion)
      {
         int tempx = (posx + stepx);
         int tempy = (posy + stepy);
         if (board[tempy % rowCount][tempx % colCount] == 0)
         {
            posx = tempx;
            posy = tempy;
            board[tempy % rowCount][tempx % colCount] = 1;
         }
      }
      else
      {
         posx = (posx + stepx);
         posy = (posy + stepy);
      }
   }
};

int main()
{

   srand(time(0));
   // initialize walkers
   Walker walkers[n_iterations][n_walkers];

   for (int i = 0; i < n_iterations; i++)
   {
      for (int j = 0; j < n_walkers; j++)
      {
         initial_data[j][0] = colCount / 2;
         initial_data[j][1] = rowCount / 2;
         walkers[i][j].posx = initial_data[j][0];
         walkers[i][j].posy = initial_data[j][1];
      }
   }

   // test board definition
   int board[rowCount][colCount];

   // result matricies initialization
   int result_matricies[n_steps][rowCount][colCount];

   // computing every step
   for (int k = 0; k < n_steps; k++)
   {
      // initializing result matricies
      for (int x = 0; x < rowCount; x++)
      {
         for (int y = 0; y < colCount; y++)
         {
            result_matricies[k][x][y] = 0;
         }
      }

      // computing iterations
      for (int i = 0; i < n_iterations; i++)
      {

         // reseting test board
         for (int x = 0; x < rowCount; x++)
         {
            for (int y = 0; y < colCount; y++)
            {
               board[x][y] = 0;
            }
         }

         // using zero testboard for movement
         for (int j = 0; j < n_walkers; j++)
         {
            walkers[i][j].move(false, board);
            int posx = walkers[i][j].posx;
            int posy = walkers[i][j].posy;
            result_matricies[k][posy % rowCount][posx % colCount] += 1;
         }
      }

      if (k % 100 == 0)
      {
         for (int x = 0; x < rowCount; x++)
         {
            for (int y = 0; y < colCount; y++)
            {
               std::cout << result_matricies[k][x][y] << " ";
            }
            std::cout << std::endl;
         }
         std::cout << std::endl;
      }
   }

   return 0;
}