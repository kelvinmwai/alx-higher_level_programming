#include "lists.h"

/**
 * insert_node - Inserts new number to sorted linked list
 * @head: pointer to linked list head
 * @number: number to be inserted
 *
 * Return: Pointer to the new node | NULL if function fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	int flag = 0;
	listint_t *new_node = NULL, *old_val = NULL, *new_val = NULL;

	if (head == NULL)
		return (NULL);
	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);
	new_node->n = number, new_node->next = NULL;
	if (*head == NULL)
	{
		*head = new_node;
		return (*head);
	}
	old_val = *head;
	if (number <= old_val->n)
	{
		new_node->next = old_val, *head = new_node;
		return (*head);
	}
	if (number > old_val->n && !old_val->next)
	{
		old_val->next = new_node;
		return (new_node);
	}
	new_val = old_val->next;
	while (old_val)
	{
		if (!new_val)
			old_val->next = new_node, flag = 1;
		else if (new_val->n == number)
			old_val->next = new_node, new_node->next = new_val, flag = 1;
		else if (new_val->n > number && old_val->n < number)
			old_val->next = new_node, new_node->next = after, flag = 1;
		if (flag)
			break;
	new_val = new_val->next, old_val = old_val->next;
	}
	return (new_node);
}
