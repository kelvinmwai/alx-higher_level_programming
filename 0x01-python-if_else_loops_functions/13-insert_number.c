#include "lists.h"
#include<stddef.h>
#include<stdlib.h>

/**
 * insert_node - Inserts new number to sorted linked list
 * @head: pointer to linked list head
 * @number: number to be inserted
 *
 * Return: Pointer to the new node | NULL if function fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;

	if (node == NULL || node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}
	while (node && node->next && node->next->n < number)
		node = node->next;

	new->next = node->next;
	node->next = new;

	return (new);
}
