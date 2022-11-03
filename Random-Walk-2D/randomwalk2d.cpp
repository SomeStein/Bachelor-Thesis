#include <iostream>
#include <cstdlib>
#include <vector>
#include <chrono>

using namespace std;

// class of Agent
class Walker
{
public:
   int posx = 0; 
   int posy = 0;

   void move(const bool size_exclusion, const vector<vector<int>> &board)
   {
      // get size of board
      int board_height = board.size();
      int board_width = board[0].size();

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
         if (board[tempy][tempx] == 0)
         {
            posx = tempx;
            posy = tempy;
         }
      }
      else
      {
         posx = (posx + stepx);
         posy = (posy + stepy);
      };
   };
};

// Matrix print function
void printMatrix(const vector<vector<int>> &matrix)
{
   int height = matrix.size();
   int width = matrix[0].size();

   for (int i = 0; i < height; i++)
   {
      for (int j = 0; j < width; j++)
      {
         cout << matrix[i][j];
         cout << " ";
      }
      cout << "\n";
   }
};

// Matrix add function
vector<vector<int>> addMatricies(vector<vector<int>> &A, vector<vector<int>> &B)
{

   // get sizes
   int rowCount = A.size();
   int colCount = A[0].size();
   vector<vector<int>> result(rowCount, vector<int>(colCount, 0));

   // check for matching sizes
   if (rowCount != B.size() || colCount != B[0].size())
   {
      throw std::runtime_error("Error, the matrix sizes do not match!");
   };

   // adding numbers and storing in result
   for (int i = 0; i < colCount; i++)
   {
      for (int j = 0; j < rowCount; j++)
      {
         result[i][j] = A[i][j] + B[i][j];
      };
   };

   return result;
};

int main()
{
   // start execution time measurement
   auto start = chrono::high_resolution_clock::now();

   // debug counter
   int counter = 0; 

   //random seed
   //srand(time(0));

   // PULL PARAMETERS FROM EXTERNAL FILE
   const int n_walkers = 10;
   const int n_steps = 100;
   const int n_iterations = 100;
   const size_t rowCount = 100;
   const size_t colCount = 10;
   int initial_data[n_walkers][2];

   // INITIALIZE AGENTS AND MATRICIES
   // zero matrix
   vector<vector<int>> zero_matrix(rowCount, vector<int>(colCount, 0));

   // agents
   Walker walkers[n_iterations][n_walkers];
   for (int i = 0; i < n_iterations; i++)
   {
      for (int j = 0; j < n_walkers; j++)
      {
         initial_data[j][0] = colCount / 2;
         initial_data[j][1] = rowCount / 2;
         walkers[i][j].posx = initial_data[j][0];
         walkers[i][j].posy = initial_data[j][1];
      };
   }

   // boards
   vector<vector<int>> boards[n_iterations];
   for (int i = 0; i < n_iterations; i++)
   {
      boards[i] = zero_matrix;
   };

   // result matricies
   vector<vector<int>> result_matricies[n_steps];
   for (int k = 0; k < n_steps; k++)
   {
      result_matricies[k] = zero_matrix;
   };

   // COMPUTE RESULTS
 
   for (int k = 0; k < n_steps; k++)
   {
      for (int i = 0; i < n_iterations; i++)
      {
         for (int j = 0; j < n_walkers; j++)
         {
            walkers[i][j].move(false, boards[i]);           
         };

      };

      //cout << "\x1B[2J\x1B[H";
      cout << k + 1 << " steps out of " << n_steps << endl;
   };

   // measure execution time
   auto stop = chrono::high_resolution_clock::now();
   auto duration = chrono::duration_cast<chrono::microseconds>(stop - start);
   cout << duration.count() / 1000000.0 << " sec" << endl;
   cout << counter << endl;
   return 0;
};
