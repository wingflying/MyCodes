#include <math.h>
#include <stdio.h>

float distance(float x1, float y1, float x2, float y2)
{
	float dx = x2 -x1;
	float dy = y2 -y1;
	float dsquared = sqrt(dx * dx + dy * dy);
	
	printf("distance is % f\n", dsquared);

	return dsquared;
}

int main(void)
{
	float point_x1, point_y1, point_x2, point_y2, dist, area;

	printf("Please input the coordinate of two points:\n");
	scanf("%f:%f:%f:%f", &point_x1, &point_y1, &point_x2, &point_y2);

	dist = distance(point_x1, point_y1, point_x2, point_y2);
	area = 3.14159 * dist * dist;

	printf("The area of the cycle is %f!\n", area);
}
