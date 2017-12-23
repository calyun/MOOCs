#include <iostream>
#include <vector>
#include <cmath>
#include <stdio.h>
using namespace std;

double getCost(vector<double> &coordsX, vector<double> &coordsY, int j, int k)
{
    double jx = coordsX[j];
    double jy = coordsY[j];
    double kx = coordsX[k];
    double ky = coordsY[k];

    return (ky-jy)*(ky-jy) + (kx-jx)*(kx-jx);
}

int TSP(vector<double> &coordsX, vector<double> &coordsY)
{
    int N = coordsX.size();
    vector<bool> visited(N, false);

    visited[0] = true;
    double total_dist = 0;

    vector<int> path = {0};
    int PS = 0;

    for (int i = 0; i < N-1; i++)
    {
        int closest = -1;
        double min_cost = 1e10;
        double cost;

        for (int j = 0; j < N; j++)
        {
            if (visited[j]) continue;
            cost = getCost(coordsX, coordsY, j, path[PS]);

            if (cost < min_cost) {
                min_cost = cost;
                closest = j;
            }
        }

        total_dist += sqrt(min_cost);
        path.push_back(closest);
        PS += 1;
        visited[closest] = true;
    }

    total_dist += sqrt(getCost(coordsX, coordsY, path[PS], path[0]));

    return (int)total_dist;
}

int main()
{
    // faster I/O
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    freopen("/home/hunteryun/Desktop/Coursera/StanfordAlgorithms/4.3.txt", "r", stdin);

    int N = 0;
    scanf("%d", &N);

    vector<double> coordsX(N);
    vector<double> coordsY(N);

    int rem;

    for (int i = 0; i < N; i++)
    {
        scanf("%d", &rem);
        scanf("%lf", &coordsX[i]);
        scanf("%lf", &coordsY[i]);
    }

    int result = TSP(coordsX, coordsY);

    printf("%d\n", result);
}
