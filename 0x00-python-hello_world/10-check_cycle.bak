#include "lists.h"

/**
 * _realloc - a function to reallocate memory is buffer array gets filled
 * Description:
 * @bufsize: size of buffer array
 * @past: buffer array
 * Return: new buffer array
 */
listint_t **_realloc(int *bufsize, listint_t **past)
{
	int n;
	listint_t **temp;

	(*bufsize) *= 2;
	temp = malloc(sizeof(listint_t *) * (*bufsize));
	if (temp == NULL)
		return (NULL);

	for (n = 0; past[n]; n++)
		temp[n] = past[n];
	temp[n] = NULL;

	free(past);
	past = temp;
	return (past);
}


/**
 * check_cycle - a function that checks for a cycle in a linked list
 * Description:
 * @list: list to be checked
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	int i, j, bufsize = 1;
	listint_t **past = malloc(sizeof(listint_t *) * bufsize);
	listint_t *current;

	if (past == NULL)
		return (-1);

	current = list;
	for (i = 0; current; i++)
	{
		past[i] = current;
		past[i + 1] = NULL;
		for (j = 0; past[j]; j++)
		{
			if (current->next == past[j])
			{
				/* printf("bufsize is: %i\n--------------------\n", bufsize); */
				free(past);
				return (1);
			}
		}
		current = current->next;
		if ((i + 2) > bufsize)
		{
			past = _realloc(&bufsize, past);
			if (past == NULL)
				return (-1);
		}
	}
	/* printf("bufsize is: %i\n--------------------\n", bufsize); */
	free(past);
	return (0);
}
