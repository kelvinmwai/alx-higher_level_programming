#include "lists.h"
#include <stdlib.h>

/**
 * check_cycle - Checks whether a singly-linked list contains a cycle
 * @list: singly-linked list to check
 *
 * Return 0 id no cycle, and 1 if a cycle is found
 */
int check_cycle(listint_t *list)
{
	listint_t *slw, *fst;

	if (list == NULL || list->next == NULL)
	       return (0);

	slw = list->next;
	fst = list->next->next;

	while (slw && fst && fst->next)
	{
		if (slw == fst)
			return (1);

		slw = slw->next;
		fst = fst->next->next;
	}

	return (0);
}
